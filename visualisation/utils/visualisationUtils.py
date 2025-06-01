import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import json
import folium



class DataVisualise:
    def __init__(self, df):
        self.df = df


    def plot_data(self, plot_type):
        if plot_type == "choropleth":
            geojson_path = "/Users/pedramjalali/Documents/data_analysis/uae_cars_analysis/visualisation/utils/uae_geojson/uae_geo.json"
            fig = px.choropleth(self.df, 
                    geojson=geojson_path, 
                    locations="Location", 
                    locationmode="geojson-id", 
                    color="Color",
                    color_continuous_scale="Viridis",
                    title="UAE Choropleth Map")

            fig.show()
            