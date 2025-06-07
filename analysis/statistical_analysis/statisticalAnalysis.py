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
        self.df = self.df.dropna(subset=['fuel_type', 'price'])

        groups = [group['price'].values for name, group in self.df.groupby('fuel_type')]
        f_stat, p_value = stats.f_oneway(*groups)

        print(f"F-statistic: {f_stat}")
        print(f"P-value: {p_value}")

        tukey = pairwise_tukeyhsd(endog=self.df['price'], groups=self.df['fuel_type'], alpha=0.05)
        print(tukey)

        if self.plot and hasattr(self.plot, 'box_plot'):
            self.plot.box_plot(
                data=self.df,
                x="fuel_type",
                y="price"
            )
