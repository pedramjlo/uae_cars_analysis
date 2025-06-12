import pandas as pd
import logging


class DataSaver:


    @staticmethod
    def save_to_csv(df, df_path, index=False):
        try:
            df.to_csv(df_path, index=index)
            logging.info(f"Data successfully saved to {df_path}")
        except Exception as e:
            logging.error(f"Failed to save data to {df_path}: {e}")
        return df
    
    

    @staticmethod
    def save_cleaning_changes(df, df_path='dataset/cleaned/cleaned_uae_cars.csv'):
        try:
            df.to_csv(df_path, index=False)
            logging.info("The cleaned dataset was successfully saved")
        except Exception as e:
            logging.error(f"Failed to save the cleaned data file: {e}")
        return df