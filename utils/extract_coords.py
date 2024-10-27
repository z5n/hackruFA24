import csv
import folium
import geopandas as gpd
import json
import pandas as pd
import random
import time
from threading import Thread
import os

file_path = f'geodata/northeast_corridor.geojson'
if os.path.exists(file_path):
    print("File found!")
else:
    print("File not found. Check the path.")

# Load the GeoJSON file to examine its structure
file_path = f'geodata/northeast_corridor.geojson'
with open(file_path, 'r') as geojson_file:
    geojson_data = json.load(geojson_file)


class Railroad:
    def __init__(self, id, name, degradation_rate):
        self.id = id
        self.name = name
        self.condition = 100  # Start at 100%
        self.degradation_rate = degradation_rate  # Degrades by this rate per second

    def degrade(self):
        self.condition = max(0, self.condition - self.degradation_rate)

def simulate_railroad_degradation(railroads):
    while True:
        for railroad in railroads:
            railroad.degrade()
            # Update color based on condition
            if railroad.condition > 70:
                railroad.color = 'green'
            elif railroad.condition > 40:
                railroad.color = 'yellow'
            else:
                railroad.color = 'red'
            
        
            save_railroad_state(railroad)
            
        time.sleep(1) 

def save_railroad_state(railroad):

    with open("railroads.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'name', 'condition', 'degradation_rate'])
        writer.writerow([railroad.id, railroad.name, railroad.condition, railroad.degradation_rate])

def load_railroad_states():
  
    railroads = []
    try:
        with open("railroads.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  
            for row in reader:
                id, name, condition, degradation_rate = row
                railroads.append(Railroad(id, name, float(degradation_rate)))
    except FileNotFoundError:
        railroads = [Railroad(1, 'Railroad 1', random.uniform(0.1, 1.0))]
    return railroads

railroads = load_railroad_states()


Thread(target=simulate_railroad_degradation, args=(railroads,)).start()


def extract_coordinates_to_csv(geojson_data, output_csv_path):
    with open(output_csv_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['latitude', 'longitude'])
        
        
        for feature in geojson_data.get("features", []):
            geometry = feature.get("geometry", {})
            coordinates = geometry.get("coordinates", [])
            
            if geometry.get("type") == "LineString":
                for lon, lat in coordinates:
                    csv_writer.writerow([lat, lon])

# Define output CSV file path
output_csv = 'coordinates.csv'
extract_coordinates_to_csv(geojson_data, output_csv)

data = pd.read_csv("coordinates.csv")
map_center = [data['latitude'].mean(), data['longitude'].mean()]
my_map = folium.Map(location=map_center, zoom_start=6)

# Create a feature group for each railroad and update based on condition
for railroad in railroads:
    folium.PolyLine(
        locations=[(row['latitude'], row['longitude']) for _, row in data.iterrows()],
        color=railroad.color,
        tooltip=f"{railroad.name}: {railroad.condition}%"
    ).add_to(my_map)

my_map.save("map.html")