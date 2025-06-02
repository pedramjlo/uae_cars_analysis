import sys
import os

# Move up two directories
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from data_visualisation.dataVisualisation import Visualisation

from descriptiveAnalysis import BrandAnalysis
import pandas as pd



if __name__ == "__main__":
    df = pd.read_csv("dataset/cleaned/cleaned_uae_cars.csv")

    visualisor = Visualisation()
    ba = BrandAnalysis(df=df, plot=visualisor)
    #ba.top_10_profitable_brands()
    #ba.least_10_profitable_brands()
    #ba.most_expensive_brands()
    #ba.least_expensive_brands()
    #ba.top_10_eco_friendly_brands()
    #ba.fuel_type_market_share_by_brand()