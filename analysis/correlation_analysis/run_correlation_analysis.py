import pandas as pd
import sys
import os

# Move up two directories
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from correlationAnalysis import CorrelationAnalysis
from data_visualisation.dataVisualisation import Visualisation

if __name__ == "__main__":
    df = pd.read_csv("dataset/cleaned/cleaned_uae_cars.csv")

    vis = Visualisation()
    corr = CorrelationAnalysis(df=df, plot=vis)

    print(corr.location_price_correlation())