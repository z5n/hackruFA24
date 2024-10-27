import csv
import folium
import json
import pandas as pd
import random
import time
from threading import Thread
import os
from bs4 import BeautifulSoup

file_path = 'geodata/northeast_corridor.geojson'
output_csv = 'coordinates.csv'

# Railroad Class for degradation
class Railroad:
    def __init__(self, id, name, degradation_rate):
        self.id = id
        self.name = name
        self.condition = 100  # Start at 100%
        self.degradation_rate = degradation_rate

    def degrade(self):
        self.condition = max(0, self.condition - self.degradation_rate)

# Railroad Simulation
def simulate_railroad_degradation(railroads):
    while True:
        for railroad in railroads:
            railroad.degrade()
            save_railroad_state(railroads)
        time.sleep(1)

# Save State
def save_railroad_state(railroads):
    with open("railroads.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'name', 'condition', 'degradation_rate'])
        for railroad in railroads:
            writer.writerow([railroad.id, railroad.name, railroad.condition, railroad.degradation_rate])

# Load State
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

# Initialize Railroads and Start Simulation
railroads = load_railroad_states()
Thread(target=simulate_railroad_degradation, args=(railroads,)).start()

# Update index.html with railroad conditions
def update_index_html(railroads):
    with open("index.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
    
    # Assuming the overview-map div should contain the railroad conditions
    map_div = soup.find("div", class_="overview-map")
    if map_div:
        condition_summary = ""
        for railroad in railroads:
            condition_summary += f"<p>{railroad.name}: {railroad.condition}% condition</p>"
        
        # Add condition summary inside overview-map div
        map_div.append(BeautifulSoup(condition_summary, "html.parser"))

    with open("index.html", "w", encoding="utf-8") as file:
        file.write(str(soup))

update_index_html(railroads)
