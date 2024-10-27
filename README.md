# HackRU Fall 24
Through this project, we aim to demonstrate the power of data visualization in improving transit accessibility and route planning for NJ TRANSIT riders.
# Overview
This project visualizes NJ TRANSIT data to map one of the largest transportation systems in the United States, focusing on geospatial data for rail lines, light rail lines, and bus routes throughout New Jersey. NJ TRANSIT operates:
- 11 commuter rail lines, 3 light rail lines, and 253 bus routes.
- A network of rail cars, light rail cars, and buses, connecting over 133 million passengers annually.

- Using NJ TRANSIT’s open datasets, our map interface displays key transit points, such as rail and light rail stations or notable bus stops, giving users a tool for exploring transit access and planning routes where data is available.
# Features
- **Interactive Map**: A detailed map showing NJ TRANSIT’s rail and light rail stations, bus terminals, and key stops across New Jersey.
- **Geospatial Data Display**: Coordinates are mapped to visualize transit points, assisting users with navigation and transit planning.
# How to Run the Project 
- **Install Dependencies**: Follow instructions to install required libraries
```$ pip install -r requirements.txt```
- **Configure the config file with your dataset**: In this case, our dataset link is `https://www.njtransit.com/rail_data.zip`.
- **Run the `gtfs-to-html` command-line utility**: Install `gtfs-to-html` from [npm](https://npmjs.org/):
```$ npm install gtfs-to-html -g```
- **Generate the map**:
```$ gtfs-to-html```
- **Run the utility file to drop the unused data from the working HTML file, and reformat the file structure**:
```$ python utils/reformat.py```
# Credits
Thanks to [gtfs-to-html](https://github.com/BlinkTagInc/gtfs-to-html), their work allowed us to visualize our dataset.