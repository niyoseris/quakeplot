# 3D Earthquake Visualization

This project visualizes earthquake data in a 3D scatter plot using Python and Plotly. The visualization focuses on earthquakes that occurred in the last week, providing an interactive way to explore seismic activity around the world.

## Features

- Displays earthquake locations in 3D space based on latitude, longitude, and depth.
- Color-coded markers represent the magnitude of each earthquake.
- Interactive visualization allows users to rotate, zoom, and hover over points to see detailed information.

## Requirements

To run this project, you need to have the following Python packages installed:

- `requests`
- `pandas`
- `plotly`
- `geopy` (if you are using distance calculations)

You can install the required packages using pip:


   pip install requests pandas plotly geopy


## How to Run

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/niyoseris/quakeplot.git
   ```

2. Navigate to the project directory:

   ```bash
   cd quakeplot
   ```

3. Run the Python script to generate the 3D earthquake visualization:

   ```bash
   python quakeplot.py
   ```

4. The generated HTML file (`quakeplot.html`) will automatically open in your web browser, displaying the 3D visualization of earthquakes.

## License

This project is licensed under the MIT License. 

## Acknowledgments

- Data is sourced from the USGS Earthquake Hazards Program.
- Special thanks to the Plotly library for providing powerful visualization tools.

## Contact

For any questions or feedback, feel free to reach out to me at [niyo.link].
