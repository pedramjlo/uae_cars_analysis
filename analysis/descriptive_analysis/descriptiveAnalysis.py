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
        
        
    def top_4_brands_yearly_sales(self):
        try:
            # Step 1: Get top 4 brands by total sales
            total_sales = (
                self.df.groupby("make")["price"]
                .sum()
                .reset_index()
                .sort_values(by='price', ascending=False)
                .head(4)
            )
            all_brands = total_sales["make"].tolist()

            # Step 2: Filter the original DataFrame to only include top 4 brands
            filtered_df = self.df[self.df["make"].isin(all_brands)]

            # Step 3: Group by brand and year to get yearly sales
            results = (
                filtered_df.groupby(["make", "year"])["price"]
                .sum()
                .reset_index()
                .sort_values(by=["make", "year"])
            )

            # Step 4: Plot
            self.plot.line_chart(
                data=results,
                x="year",
                y="price",
                color="make",
                labels={
                    "year": "Year",
                    "price": "Total Sales (AED)"
                },
                title="Top 4 Brands' Sales by Year"
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
            self.plot.line_chart(
                data=results,
                x="year",
                y="total_sales",
                labels={
                    "year": "year",
                    "total_sales": "Total Sales (AED)"
                },
                title="Sales by Year"
            )
            self.plot.bar_chart(
                data=results,
                x="year",
                y="total_sales",
                labels={
                    "year": "Year",
                    "total_sales": "Total Sales (AED)"
                },
                title="Sales by Year"
            )
            return results
        except Exception as e:
            raise e
        


    def total_sales(self):
        sales = self.df["price"].sum()
        formatted_currency = format_currency(sales, 'AED', locale='en_AE')
        return formatted_currency
        


class CityAnalysis:
    def __init__(self, df, plot=None):
        self.df = df
        self.plot = plot

    
    @staticmethod
    def normalise_city_name(city):
        return " ".join(seg.capitalize() for seg in city.split(" "))
    


    @staticmethod
    def normalise_brand_name(brand):
        return "-".join(seg for seg in brand.split(" "))
        



    def revenue_per_city(self):
        try:
            results = (
                self.df.groupby("location")["price"]
                .sum()
                .reset_index()
                .sort_values(by="price", ascending=False)
            )
            self.plot.bar_chart(
                data=results,
                x="location",
                y="price",
                labels={
                    "location": "City",
                    "price": "Total Sales (AED)"
                },
                title="Revenue per City"
            )
            return results
        except Exception as e:
            raise e
        


    def top_selling_brands_per_city(self, city_name):
        city_name = CityAnalysis.normalise_city_name(city_name)
        try:
            if city_name:
                city_data = self.df[self.df["location"] == city_name]
                results = (
                    city_data.groupby("make")["price"]
                    .sum()
                    .reset_index()
                    .sort_values(by="price", ascending=False)
                )
                self.plot.bar_chart(
                data=results,
                x="make",
                y="price",
                labels={
                    "make": "Car Brand",
                    "price": f"Total Sales in {city_name} (AED)"
                },
                title=f"Top Selling Brands in {city_name}"
            )

            return results
        except Exception as e:
            raise e
        
        

    def fuel_type_sales_per_city(self, city_name):
        city_name = CityAnalysis.normalise_city_name(city_name)
        try:
            if city_name:
                city_data = self.df[self.df["location"] == city_name]
                results = (
                    city_data.groupby("fuel_type")["price"]
                    .sum()
                    .reset_index()
                    .sort_values(by="price", ascending=False)
                )
                self.plot.pie_chart(
                data=results,
                values="price",
                names="fuel_type",
                labels={
                    "fuel_type": "Fuel Type",
                    "price": f"Total Sales in {city_name} (AED)"
                },
                title=f"Fuel Type Sales in {city_name}"
            )

            return results
        except Exception as e:
            raise e
            


    def top_10_selling_cars_per_city(self, city_name):

        city_name = CityAnalysis.normalise_city_name(city_name)

        self.df["vehicle"] = (
                self.df["make"] + " " +
                self.df["model"] + " " +
                self.df["year"].astype(str)
            )

        try:
            city_data = self.df[self.df["location"] == city_name]
            
            if city_data.empty:
                return f"No sales data available for {city_name}."

            results = (
                city_data.groupby("vehicle")["price"]
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
                    "model": "Car Model",
                    "price": f"Total Sales in {city_name} (AED)"
                },
                title=f"Top Selling Models in {city_name}"
            )

            return results if results is not None else "No valid results."
    
        except Exception as e:
            return f"Error processing data: {str(e)}"



    def vehicle_type_sales_per_city(self, city_name):
        city_name = CityAnalysis.normalise_city_name(city_name)
        try:
            if city_name:
                city_data = self.df[self.df["location"] == city_name]
                results = (
                    city_data.groupby("body_type")["price"]
                    .sum()
                    .reset_index()
                    .sort_values(by="price", ascending=False)
                )
                self.plot.pie_chart(
                data=results,
                values="price",
                names="body_type",
                labels={
                    "body_type": "Vehicle Type",
                    "price": f"Total Sales in {city_name} (AED)"
                },
                title=f"Vehicle Type Sales in {city_name}"
            )

            return results
        except Exception as e:
            raise e


 
    def median_brand_prices_per_city(self, city_name, brand_name):
        city_name = CityAnalysis.normalise_city_name(city_name)
        brand_name = CityAnalysis.normalise_brand_name(brand_name)

        try:
            if city_name and brand_name:
                # Filter for rows where BOTH city and brand match
                filtered_data = self.df[
                    (self.df["location"] == city_name) &
                    (self.df["make"] == brand_name)
                ]

                if filtered_data.empty:
                    return f"No data for {brand_name} in {city_name} was recorded" 

                # Extract prices and calculate median
                median_price = filtered_data["price"].median()

                formatted_result = format_currency(median_price, 'AED', locale='en_AE')
                return f"The median price for {brand_name} vehicles in {city_name}; {formatted_result}"

            else:
                return None

        except Exception as e:
            raise e

            