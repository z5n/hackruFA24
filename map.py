import csv
import folium
import geopandas as gpd
import json
import pandas as pd

# Load the GeoJSON file to examine its structure
file_path = 'maps/northeasterncorridor.geojson'
with open(file_path, 'r') as geojson_file:
    geojson_data = json.load(geojson_file)

# Function to extract coordinates and save them as a CSV
def extract_coordinates_to_csv(geojson_data, output_csv_path):
    with open(output_csv_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['latitude', 'longitude'])
        
        # Iterate through each feature in the GeoJSON
        for feature in geojson_data.get("features", []):
            # Extract the coordinates from the geometry
            geometry = feature.get("geometry", {})
            coordinates = geometry.get("coordinates", [])
            
            # Depending on the "type" (e.g., Point, LineString, etc.), handle coordinates
            if geometry.get("type") == "Point":
                # Single pair of coordinates
                lon, lat = coordinates
                csv_writer.writerow([lat, lon])
            elif geometry.get("type") == "LineString":
                # Multiple pairs of coordinates
                for lon, lat in coordinates:
                    csv_writer.writerow([lat, lon])
            elif geometry.get("type") == "MultiLineString":
                # Multiple sets of LineString coordinates
                for line in coordinates:
                    for lon, lat in line:
                        csv_writer.writerow([lat, lon])

# Define output CSV file path
output_csv = 'coordinates.csv'

# Extract and write coordinates to CSV
extract_coordinates_to_csv(geojson_data, output_csv)

data = pd.read_csv("coordinates.csv")
map_center = [data['latitude'].mean(), data['longitude'].mean()]
my_map = folium.Map(location=map_center, zoom_start=6)
for index, row in data.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']], 
    ).add_to(my_map)

    if index == 100:
        break
my_map.save("map.html")