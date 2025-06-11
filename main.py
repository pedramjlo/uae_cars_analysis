from data_loading.dataLoading import DataLoader
from data_cleaning.dataCleaning import DataCleaner
from data_saving.dataSaving import DataSaver



class Pipeline:
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
    

    def get_columns(self):
        print(self.cleaned_data.columns)

    

    # CENTRAL FUNCTION TO RUN ALL PIPELINE METHODS AT ONCE
    def run(self):
        pass


if __name__ == "__main__":
    raw_data = "dataset/raw/uae_used_cars.csv"
    pl = Pipeline(raw_dataset=raw_data)
    pl.load_data()
    pl.run_cleaner()
    pl.save_cleaned_data()
    pl.get_columns()
