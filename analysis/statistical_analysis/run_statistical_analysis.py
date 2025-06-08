import pandas as pd
import sys
import os

# Move up two directories
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from analysis.statistical_analysis.statisticalAnalysis import StatisticalAnalysis
from data_visualisation.dataVisualisation import Visualisation


if __name__ == "__main__":
    df = pd.read_csv("dataset/cleaned/cleaned_uae_cars.csv")

    vis = Visualisation()
    sa = StatisticalAnalysis(df=df, plot=vis)

    print(sa.fuel_type_to_price_anova())