from data_loading.dataLoading import DataLoader
from data_cleaning.dataCleaning import DataCleaner
from data_saving.dataSaving import DataSaver

# CLUSTERING ANALYSIS MODULES
from analysis.clustering_analysis.brandClusteringAnalysis import BrandClustering

class Pipeline:
    def __init__(self, raw_dataset):
        self.raw_dataset = raw_dataset
        self.loaded_raw_data = None
        self.cleaned_data = None

    def load_data(self):
        loader = DataLoader(self.raw_dataset)
        self.loaded_raw_data = loader.read_data()


    def run_cleaner(self):
        cleaner = DataCleaner(raw_dataset=self.loaded_raw_data)
        self.cleaned_data = cleaner.clean_all()
    

    def save_cleaned_data(self):
        saver = DataSaver(cleaned_data=self.cleaned_data)
        return saver.save_changes()
    

    def run_clustering_analysis(self, clustering_analysis_type="by_sales"):
        brand_clustering = BrandClustering(df=self.cleaned_data)
        
        if clustering_analysis_type == "by_sales":
            clustered_data, model = brand_clustering.cluster_by_sales()
            print(clustered_data, model)  # or store/use it

    

    # CENTRAL FUNCTION TO RUN ALL PIPELINE METHODS AT ONCE
    def run(self):
        pass


if __name__ == "__main__":
    raw_data = "dataset/raw/uae_used_cars.csv"
    pl = Pipeline(raw_dataset=raw_data)
    pl.load_data()
    pl.run_cleaner()
    pl.save_cleaned_data()
    pl.run_clustering_analysis()