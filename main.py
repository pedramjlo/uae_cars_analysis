from loading.dataLoading import DataLoader
from data_cleaning.dataCleaning import DataCleaner
from saving.dataSaving import DataSaver

if __name__ == "__main__":
    raw_dataset = "dataset/raw/uae_used_cars.csv"


    # LOADING THE RAW DATASET 
    loader = DataLoader(raw_dataset=raw_dataset)
    loaded_raw_data = loader.read_data()


    # CLEANING THE RAW DATASET
    cleaner = DataCleaner(raw_dataset=loaded_raw_data)
    cleaned_data = cleaner.clean_all()

    
    

    # SAVING THE CLEANED DATA
    saver = DataSaver(cleaned_data=cleaned_data)
    saver.save_changes()


