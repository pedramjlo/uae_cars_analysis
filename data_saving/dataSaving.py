import pandas as pd
import logging


class DataSaver:
    df_path='dataset/cleaned/cleaned_uae_cars.csv' 

    @staticmethod
    def save_to_csv(df, index=False):
        try:
            df.to_csv(index=index)
            logging.info(f"Data successfully saved to {DataSaver.df_path}")
        except Exception as e:
            logging.error(f"Failed to save data to {DataSaver.df_path}: {e}")
        return df
    
    

    @staticmethod
    def save_cleaning_changes(df):
        try:
            df.to_csv(DataSaver.df_path, index=False)
            logging.info("The cleaned dataset was successfully saved")
        except Exception as e:
            logging.error(f"Failed to save the cleaned data file: {e}")
        return df