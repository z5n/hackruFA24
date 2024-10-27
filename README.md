# HackRU Fall 24
Through this project, we aim to create an interactive map tool purposed for displaying the degradation of each of NJ TRANSIT’s railways, giving users a tool for understanding where maintenance is needed.
# Overview
This project visualizes NJ TRANSIT data to map one of the largest transportation systems in the United States, focusing on geospatial data for rail lines. NJ TRANSIT operates:
- 11 commuter rail lines, 3 light rail lines, and 253 bus routes.
- A network of rail cars, light rail cars, and buses, connecting over 133 million passengers annually.
### Inspiration
Our team was inspired by NJ TRANSIT’s commitment to innovation and their open data challenge at HackRU Fall 2024. We wanted to create an accessible tool that helps the NJ Transit team understand what part of their railways need, or will be needing maintenance.
### What We Learned
Working on this project taught us how to handle geospatial data, design interactive maps, and process large datasets for meaningful visualizations. We gained experience in working with map libraries and improved our skills in front-end design for intuitive user interfaces.
### How We Built the Project
The project was built using a combination of:
- **Python** for backend processing and handling data from NJ TRANSIT’s dataset.
- **JavaScript and Leaflet.js** to create an interactive map where users can explore railways, and view the estimated health of each railway.
- **HTML/CSS** for structuring and styling the interface, making it visually engaging and easy to navigate.
- **gtfs-to-html** for converting NJ Transit's provided railway dataset to HTML, allowing for a visualization of their railways on a map.
### Challenges We Faced
1. **Data Cleaning**: Integrating NJ TRANSIT’s data was challenging due to inconsistencies and the need for precise geospatial alignment.
2. **Map Responsiveness**: Ensuring the map looked good on various devices required multiple adjustments to CSS and JavaScript for smooth interactivity.
# Features
- **Interactive Map**: A detailed map showing NJ TRANSIT’s railways, and key stops across New Jersey.
- **Geospatial Data Display**: Coordinates are mapped to visualize transit points, for better understanding of where along the railway maintenance is needed.
# How to Run the Project 
- **Install Dependencies**: Install the required packages.
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
