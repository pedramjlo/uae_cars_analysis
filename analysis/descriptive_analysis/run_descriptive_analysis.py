import sys
import os

# Move up three directories
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from data_visualisation.dataVisualisation import Visualisation

from descriptiveAnalysis import BrandAnalysis
import pandas as pd



if __name__ == "__main__":
    df = pd.read_csv("dataset/cleaned/cleaned_uae_cars.csv")

    visualisor = Visualisation()
    ba = BrandAnalysis(df=df, plot=visualisor)
    ba.top_10_profitable_brands()