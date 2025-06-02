from babel.numbers import format_currency




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
        

    def least_10_profitable_brands(self):
        try:
            results = (
                self.df.groupby("make")["price"]
                .sum()
                .reset_index()
                .sort_values(by='price', ascending=False)
                .tail(10) 
            )
            self.plot.bar_chart(
                data=results, 
                x="make", 
                y="price", 
                labels={
                    "make": "Car Brand",
                    "price": "Total Sales (AED)"
                },
                title="Top 10 Least Profitable Brands"
            )
            
            return results
        except Exception as e:
            raise e
        

    def top_10_expensive_brands(self):
        try:
            results = (
                self.df.groupby("make")["price"]
                .median()
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
                    "price": "Median Prices (AED)"
                },
                title="Top 10 Most Expensive Brands"
            )
            return results
        except Exception as e:
            raise e
        

    def least_10_expensive_brands(self):
        try:
            results = (
                self.df.groupby("make")["price"]
                .median()
                .reset_index()
                .sort_values(by='price', ascending=False)
                .tail(10) 
            )

            self.plot.bar_chart(
                data=results, 
                x="make", 
                y="price", 
                labels={
                    "make": "Car Brand",
                    "price": "Median Prices (AED)"
                },
                title="Top 10 Least Expensive Brands"
            )
            return results
        except Exception as e:
            raise e
        

    def top_10_eco_friendly_brands(self):
        try:
            electric_type = self.df[self.df['fuel_type'].str.lower() == 'electric']
            results = (
                electric_type.groupby("make")
                .size()
                .reset_index(name='eco_model_count')
                .sort_values(by='eco_model_count', ascending=False)
            )

            self.plot.bar_chart(
                data=results, 
                x="make", 
                y="eco_model_count", 
                labels={
                    "make": "Car Brand",
                    "eco_model_count": "Number of EV Models"
                },
                title="Top 10 Most Eco-Friendly Brands"
            )
            return results
        except Exception as e:
            raise e
        


class VehicleAnalysis:
    def __init__(self, df, plot):
        self.df = df
        self.plot = plot


    def top_10_most_expensive_cars(self):
        try:
            
            self.df["Vehicle"] = (
                self.df["make"] + " " +
                self.df["model"] + " " +
                self.df["year"].astype(str)
            )
            

            # Sort by price and take the top 10 rows directly
            results = (
                self.df.sort_values(by="price", ascending=False)
                    .head(10)[["Vehicle", "price"]]
            )

            self.plot.bar_chart(
                data=results,
                x="Vehicle",
                y="price",
                labels={
                    "model": "Vehicle",
                    "price": "Price (AED)"
                },
                title="Top 10 Most Expensive Cars"
            )

            return results
        except Exception as e:
            raise e
        

    def top_10_least_expensive_cars(self):
        try:
            
            self.df["Vehicle"] = (
                self.df["make"] + " " +
                self.df["model"] + " " +
                self.df["year"].astype(str)
            )
            

            # Sort by price and take the top 10 rows directly
            results = (
                self.df.sort_values(by="price", ascending=False)
                    .tail(10)[["Vehicle", "price"]]
            )

            self.plot.bar_chart(
                data=results,
                x="Vehicle",
                y="price",
                labels={
                    "model": "Vehicle",
                    "price": "Price (AED)"
                },
                title="Top 10 Least Expensive Cars"
            )

            return results
        except Exception as e:
            raise e



    def top_10_profitable_cars(self):
        try:
            
            self.df["vehicle"] = (
                self.df["make"] + " " +
                self.df["model"] + " " +
                self.df["year"].astype(str)
            )
            

            # Sort by price and take the top 10 rows directly
            results = (
                self.df.groupby("vehicle")["price"]
                .sum()
                .reset_index()
                .sort_values(by="price", ascending=False)
                .head(10)
            )

            self.plot.bar_chart(
                data=results,
                x="vehicle",
                y="price",
                labels={
                    "vehicle": "vehicle",
                    "price": "Total Sales (AED)"
                },
                title="Top 10 Most Profitable Cars"
            )

            return results
        except Exception as e:
            raise e
        
        
    def least_10_profitable_cars(self):
        try:
            
            self.df["vehicle"] = (
                self.df["make"] + " " +
                self.df["model"] + " " +
                self.df["year"].astype(str)
            )
            

            # Sort by price and take the top 10 rows directly
            results = (
                self.df.groupby("vehicle")["price"]
                .sum()
                .reset_index()
                .sort_values(by="price", ascending=False)
                .tail(10)
            )

            self.plot.bar_chart(
                data=results,
                x="vehicle",
                y="price",
                labels={
                    "vehicle": "vehicle",
                    "price": "Total Sales (AED)"
                },
                title="Top 10 Least Profitable Cars"
            )

            return results
        except Exception as e:
            raise e



            




class SalesAnalysis:
    def __init__(self, df, plot=None):
        self.df = df
        self.plot = plot


    def sales_by_year(self):
        try:
            self.df = self.df.rename(columns={"price": "total_sales"})
            results = (
                self.df.groupby("year")["total_sales"]
                .sum()
                .reset_index()
                .sort_values(by='year', ascending=True)
            )            
            return results
        except Exception as e:
            raise e
        


    def total_sales(self):
        sales = self.df["price"].sum()
        formatted_currency = format_currency(sales, 'AED', locale='en_AE')
        return formatted_currency
        


class CityAnalysis:
    def __init__(self, df):
        self.df = df