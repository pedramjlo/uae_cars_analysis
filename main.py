import pandas as pd

from data_loading.dataLoading import DataLoader
from data_cleaning.dataCleaning import DataCleaner
from data_saving.dataSaving import DataSaver


from data_visualisation.dataVisualisation import Visualisation

from analysis.descriptive_analysis.descriptiveAnalysis import BrandAnalysis
from analysis.descriptive_analysis.descriptiveAnalysis import VehicleAnalysis
from analysis.descriptive_analysis.descriptiveAnalysis import SalesAnalysis
from analysis.descriptive_analysis.descriptiveAnalysis import CityAnalysis
from analysis.descriptive_analysis.distributionAnalysis import Distribution
from analysis.descriptive_analysis.distributionAnalysis import Skewness


from data_scaling.dataProcessing import DataScaler




class CleanerPipeline:
    def __init__(self, raw_dataset):
        self.raw_dataset = raw_dataset
        self.loaded_raw_data = None
        self.cleaned_data = None

    def load_data(self):
        loader = DataLoader(self.raw_dataset)
        self.loaded_raw_data = loader.read_data()


    def run_cleaner(self):
        cleaner = DataCleaner(raw_dataset=pl.loaded_raw_data)
        self.cleaned_data = cleaner.clean_all()
    

    def save_cleaned_data(self):
        saver = DataSaver(cleaned_data=self.cleaned_data)
        return saver.save_cleaning_changes()
    

    

    # CENTRAL FUNCTION TO RUN ALL PIPELINE METHODS AT ONCE
    def run(self):
        pass


if __name__ == "__main__":
    raw_data = "dataset/raw/uae_used_cars.csv"
    #pl = CleanerPipeline(raw_dataset=raw_data)
    #pl.load_data()
    #pl.run_cleaner()
    #pl.save_cleaned_data()


    visualisor = Visualisation()


    df = pd.read_csv("dataset/cleaned/cleaned_uae_cars.csv")


    # DESCRIPTIVE ANALYSIS METHODS
    ba = BrandAnalysis(df=df, plot=visualisor)
    median_prices_df = ba.median_prices()
    #ba.top_10_profitable_brands()
    #ba.least_10_profitable_brands()
    #ba.top_10_expensive_brands()
    #ba.least_expensive_brands()
    #ba.top_10_eco_friendly_brands()
    #ba.least_eco_friendly_brands()
    #ba.fuel_type_market_share_by_brand()
    #ba.top_4_brands_yearly_sales()
    #print(ba.get_sales_trend(brand_name="rolls-royce"))
    #ba.median_prices()



    va = VehicleAnalysis(df=df, plot=visualisor)
    #va.top_10_most_expensive_cars()
    #va.top_10_least_expensive_cars()
    #va.top_10_profitable_cars()
    #va.least_10_profitable_cars()
    #va.median_vehicle_price_by_body_type()
    #va.median_vehicle_price_by_fuel_type()
    #print(va.vehicle_sales_count_by_fuel_type())


    sales = SalesAnalysis(df=df, plot=visualisor)
    #print(sales.total_sales())
    #print(sales.sales_by_year())
    #sales.sales_by_year()
    #sales.sales_by_fuel_type()



    city = CityAnalysis(df=df, plot=visualisor)
    #city.revenue_per_city()
    #city.top_selling_brands_per_city(city_name=input("enter city: "))
    #city.fuel_type_sales_per_city(city_name=input("enter city: "))
    #print(city.top_10_selling_cars_per_city(city_name=input("enter city: ")))
    #city.vehicle_type_sales_per_city(city_name=input("enter city: "))
    #print(city.median_brand_prices_per_city(city_name=input("enter city: "), brand_name=input("enter brand: ")))
    #city.most_popular_colors(city_name=input("enter city: "))


    distro = Distribution(df=df, plot=visualisor)
    prices_std = distro.get_std(group_by_col="make", target_col="price")



    sk = Skewness(df=df, plot=visualisor)
    prices_skewness = sk.get_skewness(group_by_col="make", target_col="price")



    # MERGING MEDIAN PRICES, STD, AND SKEWNESS
    prices_metrics_df = prices_std.merge(prices_skewness, on='make').merge(median_prices_df, on='make')




    # DATA PROCESSING
    scaler = DataScaler(strategy="standard")
    scaler.fit(prices_metrics_df.drop(columns="make"))
    scaled_data = scaler.transform(prices_metrics_df.drop(columns='make'))
    print(scaled_data)

