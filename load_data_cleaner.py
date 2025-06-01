from data_cleaning.dataCleaning import DataCleaner


# CLEANING THE RAW DATASET
cleaner = DataCleaner(raw_dataset=loaded_raw_data)
cleaned_data = cleaner.clean_all()