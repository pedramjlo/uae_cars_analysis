import pandas as pd
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd





class StatisticalAnalysis:
    def __init__(self, df, plot=None):
        self.df = df
        self.plot = plot

    @staticmethod
    def interpret_correlation(score):
        correlation_strength = {
            (0.9, 1.01): "Very strong positive correlation",
            (0.7, 0.9): "Strong positive correlation",
            (0.5, 0.7): "Moderate positive correlation",
            (0.3, 0.5): "Weak positive correlation",
            (0.0, 0.3): "Very weak or no correlation",
            (-0.3, 0.0): "Very weak or no correlation",
            (-0.5, -0.3): "Weak negative correlation",
            (-0.7, -0.5): "Moderate negative correlation",
            (-0.9, -0.7): "Strong negative correlation",
            (-1.01, -0.9): "Very strong negative correlation",
        }


        for (low, high), description in correlation_strength.items():
            if low <= score <= high:
                return description
        return "Invalid correlation score"



    # T-TEST METHOD SINCE ONLY PRICE AND MILEAGE ARE TAKEN INTO ACCOUNT
    def fuel_type_to_price_anova(self):
        vehicle_sales = self.df.groupby(['fuel_type', 'make', 'model', 'year']).size().reset_index(name='sales_count')

        # perform ANOVA
        groups = [group['sales_count'].values for name, group in vehicle_sales.groupby('fuel_type')]
        f_stat, p_value = stats.f_oneway(*groups)

        print(f"F-statistic: {f_stat}")
        print(f"P-value: {p_value}")




        if p_value < 0.05:
            tukey = pairwise_tukeyhsd(endog=vehicle_sales['sales_count'], groups=vehicle_sales['fuel_type'], alpha=0.05)
            print(tukey.summary())
        else:
            print("No significant difference found in ANOVA; skipping Tukey test.")