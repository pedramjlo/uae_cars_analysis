



class BrandAnalysis:
    def __init__(self, df, plot):
        self.df = df
        self.plot = plot


    def top_10_profitable_brands(self):
        try:
            results = (
                self.df.groupby("Make")["Price"]
                .sum()
                .reset_index()
                .sort_values(by='Price', ascending=False)
                .head(10) 
            )
            self.plot.bar_chart(data=results, x="Make", y="Price")
            return results
        except Exception as e:
            raise e



class SalesAnalysis:
    def __init__(self, df):
        self.df = df


class CityAnalysis:
    def __init__(self, df):
        self.df = df