import pandas as pd
import logging

class DataSaver:
    def __init__(self, cleaned_data: pd.DataFrame):
        self.cleaned_data = cleaned_data


    def save_cleaning_changes(self, cleaned_data_path='dataset/cleaned/cleaned_uae_cars.csv'):
        try:
            self.cleaned_data.to_csv(cleaned_data_path, index=False)
            logging.info("The cleaned dataset was successfully saved")
        except Exception as e:
            logging.error(f"Failed to save the cleaned data file: {e}")
        return self