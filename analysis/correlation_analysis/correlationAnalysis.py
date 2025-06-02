import pandas as pd

class CorrelationAnalysis:
    def __init__(self, df, plot=None):
        self.df = df
        self.plot = plot

    def interpret_correlation(self, score):
        correlation_strength = {
            (0.9, 1.0): "Very strong positive correlation",
            (0.7, 0.9): "Strong positive correlation",
            (0.5, 0.7): "Moderate positive correlation",
            (0.3, 0.5): "Weak positive correlation",
            (0.0, 0.3): "Very weak or no correlation",
            (-0.3, 0.0): "Very weak or no correlation",
            (-0.5, -0.3): "Weak negative correlation",
            (-0.7, -0.5): "Moderate negative correlation",
            (-0.9, -0.7): "Strong negative correlation",
            (-1.0, -0.9): "Very strong negative correlation",
        }

        for (low, high), description in correlation_strength.items():
            if low <= score <= high:
                return description
        return "Invalid correlation score"


    def location_price_correlation(self):
        try:
            # Step 1: Calculate correlation between location codes and median prices
            median_prices = (
                self.df.groupby("location")["price"]
                .median()
                .reset_index()
                .rename(columns={"price": "median_price"})
            )

            median_prices["location_code"] = median_prices["location"].astype("category").cat.codes
            correlation_score = median_prices["location_code"].corr(median_prices["median_price"])

            # Step 2: Plot box plot using raw data
            self.plot.box_plot(
                data=self.df,
                x="location",
                y="price",
                title="Price Distribution Across Cities",
                labels={
                    "location": "Location",
                    "price": "Price (AED)"
                }
            )

            return correlation_score
        except Exception as e:
            raise e

