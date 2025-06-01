



class BrandAnalysis:
    def __init__(self, df, plot):
        self.df = df
        self.plot = plot


    def top_10_profitable_brands(self):
        try:
            results = (
                self.df.groupby("make")["price"]
                .sum()
                .reset_index()
                .sort_values(by='price', ascending=False)
                .head(10) 
            )
            self.plot.bar_chart(
                data=results, 
                x="make", 
                y="price", 
                labels={
                    "make": "Car Brand",
                    "price": "Total Sales (AED)"
                },
                title="Top 10 Most Profitable Brands"
                )
            
            return results
        except Exception as e:
            raise e



class SalesAnalysis:
    def __init__(self, df):
        self.df = df


class CityAnalysis:
    def __init__(self, df):
        self.df = df