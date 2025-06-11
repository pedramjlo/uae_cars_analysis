"""
processing the skewness, standard deviation, and median prices for data scaling
"""

import sys
import os

# Move up two directories
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))



from analysis.descriptive_analysis.descriptiveAnalysis import BrandAnalysis # median prices method
from analysis.descriptive_analysis.distributionAnalysis import Distribution
from analysis.descriptive_analysis.distributionAnalysis import Skewness



class DataProcessing:
    def __init__(self, brand_analysis, brand_std, brand_skew):
        self.brand_analysis = brand_analysis
        self.brand_std = brand_std
        self.brand_skew = brand_skew
    
    def process(self):
        try:
            median_prices = BrandAnalysis.median_prices()
            std = Distribution.get_std(group_by_col="make", target_col="price")
            skew = Skewness.get_skewness(group_by_col="make", target_col="price")

            print(median_prices, std, skew)

        except Exception as e:
            raise e






p = DataProcessing()
p.process()