import pandas as pd
import logging


class DataSaver:


    @staticmethod
    def save_cleaning_changes(df, df_path='dataset/cleaned/cleaned_uae_cars.csv'):
        try:
            df.to_csv(df_path, index=False)
            logging.info("The cleaned dataset was successfully saved")
        except Exception as e:
            logging.error(f"Failed to save the cleaned data file: {e}")
        return df
