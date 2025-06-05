import sys
import os

# Move up two directories
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from data_visualisation.dataVisualisation import Visualisation

from descriptiveAnalysis import BrandAnalysis
from descriptiveAnalysis import VehicleAnalysis
from descriptiveAnalysis import SalesAnalysis
from descriptiveAnalysis import CityAnalysis

import pandas as pd



if __name__ == "__main__":
    df = pd.read_csv("dataset/cleaned/cleaned_uae_cars.csv")

    visualisor = Visualisation()

    ba = BrandAnalysis(df=df, plot=visualisor)
    va = VehicleAnalysis(df=df, plot=visualisor)
    sales = SalesAnalysis(df=df, plot=visualisor)
    city = CityAnalysis(df=df, plot=visualisor)


    # BRAND ANALYSIS
    #ba.top_10_profitable_brands()
    #ba.least_10_profitable_brands()
    #ba.top_10_expensive_brands()
    #ba.least_expensive_brands()
    #ba.top_10_eco_friendly_brands()
    #ba.fuel_type_market_share_by_brand()
    #ba.top_4_brands_yearly_sales()


    # VEHICLE ANALYSIS
    #va.top_10_most_expensive_cars()
    #va.top_10_least_expensive_cars()
    #va.top_10_profitable_cars()
    #va.least_10_profitable_cars()


    # SALES ANALYSIS
    #print(sales.total_sales())
    #print(sales.sales_by_year())
    #sales.sales_by_year()
    

    # CITY ANALYSIS
    #city.revenue_per_city()
    #city.top_selling_brands_per_city(city_name=input("enter city: "))
    #city.fuel_type_sales_per_city(city_name=input("enter city: "))
    #print(city.top_10_selling_cars_per_city(city_name=input("enter city: ")))
    #city.vehicle_type_sales_per_city(city_name=input("enter city: "))
    print(city.median_brand_prices_per_city(city_name=input("enter city: "), brand_name=input("enter brand: ")))