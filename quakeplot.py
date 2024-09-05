# quakeplot.py

import requests
import pandas as pd
import plotly.express as px
import plotly.offline as pyo
from geopy.distance import great_circle

def fetch_earthquake_data():
    """Fetch earthquake data from the USGS API for the last week."""
    response = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson")
    return response.json()['features']

def filter_earthquakes(data, center_coordinates=None, radius_km=None):
    """Filter earthquakes based on location and radius."""
    filtered_data = []
    for earthquake in data:
        latitude = earthquake['geometry']['coordinates'][1]
        longitude = earthquake['geometry']['coordinates'][0]
        depth = earthquake['geometry']['coordinates'][2]
        magnitude = earthquake['properties']['mag']
        location = earthquake['properties']['place']
        
        if center_coordinates and radius_km:
            # Filter based on distance from the center coordinates
            if great_circle(center_coordinates, (latitude, longitude)).kilometers <= radius_km:
                filtered_data.append({"latitude": latitude, "longitude": longitude, "depth": depth, "magnitude": magnitude, "location": location})
        else:
            # Include all earthquakes if no filter is applied
            filtered_data.append({"latitude": latitude, "longitude": longitude, "depth": depth, "magnitude": magnitude, "location": location})

    return pd.DataFrame(filtered_data)

def create_3d_plot(df, title):
    """Create a 3D scatter plot of earthquake data."""
    fig = px.scatter_3d(df, x='longitude', y='latitude', z='depth',
                         color='magnitude',  # Color by magnitude
                         hover_name='location',
                         labels={'longitude': 'Longitude', 'latitude': 'Latitude', 'depth': 'Depth (km)', 'magnitude': 'Magnitude'},
                         title=title,
                         color_continuous_scale=px.colors.sequential.Viridis)

    # Reverse the Z axis to show depth correctly
    fig.update_layout(scene=dict(zaxis=dict(title='Depth (km)', autorange='reversed')))
    return fig

def main():
    # Fetch earthquake data
    earthquake_data = fetch_earthquake_data()

    # Filter for earthquakes around Cyprus (1000 km radius)
    cyprus_coordinates = (35.0, 33.0)  # (latitude, longitude)
    cyprus_earthquakes = filter_earthquakes(earthquake_data, center_coordinates=cyprus_coordinates, radius_km=1000)

    # Create 3D plot for Cyprus earthquakes
    cyprus_plot = create_3d_plot(cyprus_earthquakes, title='Earthquakes within 1000 km of Cyprus (3D Plot)')
    pyo.plot(cyprus_plot, filename='cyprus_earthquakes_3d_plot.html', auto_open=True)

    # Create 3D plot for all earthquakes
    all_earthquakes = filter_earthquakes(earthquake_data)
    all_plot = create_3d_plot(all_earthquakes, title='All Earthquakes in the Last Week (3D Plot)')
    pyo.plot(all_plot, filename='all_earthquakes_3d_plot.html', auto_open=True)

if __name__ == '__main__':
    main()
