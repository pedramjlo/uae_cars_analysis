import sys
import os

# Move up two directories
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from data_visualisation.dataVisualisation import Visualisation

from descriptiveAnalysis import BrandAnalysis
from  descriptiveAnalysis import VehicleAnalysis

import pandas as pd



if __name__ == "__main__":
    df = pd.read_csv("dataset/cleaned/cleaned_uae_cars.csv")

    visualisor = Visualisation()

    ba = BrandAnalysis(df=df, plot=visualisor)
    va = VehicleAnalysis(df=df, plot=visualisor)


    # BRAND ANALYSIS
    #ba.top_10_profitable_brands()
    #ba.least_10_profitable_brands()
    #ba.top_10_expensive_brands()
    #ba.least_expensive_brands()
    #ba.top_10_eco_friendly_brands()
    #ba.fuel_type_market_share_by_brand()


    # VEHICLE ANALYSIS
    #va.top_10_most_expensive_cars()
    va.top_10_least_expensive_cars()