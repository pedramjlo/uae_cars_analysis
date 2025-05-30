import pandas as pd
import numpy as np
import logging

logging.basicConfig(
    level=logging.INFO,  # Set the minimum log level
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log message format
    # filename='app.log'  # Log to a file (optional)
)



class DataCleaner:
    
    def __init__(self, raw_dataset: pd.DataFrame):
        self.raw_dataset = raw_dataset

    
    def strip_spaces(self):
        try:
            self.raw_dataset['Location'] = self.raw_dataset['Location'].str.strip()
            self.raw_dataset['Description'] = self.raw_dataset['Description'].str.strip()
            logging.info("Successfully stripped spaces")
        except Exception as e:
            logging.error(f"Failed to strip some white spaces: {e}")
        
        return self

    
    def titlise_columns(self):
        try:
            self.raw_dataset['Make'] = self.raw_dataset['Make'].str.title()
            self.raw_dataset['Model'] = self.raw_dataset['Model'].str.title()
            self.raw_dataset['Location'] = self.raw_dataset['Location'].str.title()
            logging.info("Successfully titlised columns")
        except Exception as e:
            logging.error(f"Failed to titlise some columns: {e}")
        return self
        

    def convert_to_string(self):
        try:
            # Select columns with object or mixed types
            string_like_cols = self.raw_dataset.select_dtypes(include=['object']).columns
            self.raw_dataset[string_like_cols] = self.raw_dataset[string_like_cols].astype(str)
            logging.info(f"Successfully converted object-type columns to string: {list(string_like_cols)}")
        except Exception as e:
            logging.error(f"Error converting columns to string: {e}")
        return self


    def convert_all_possible_to_integer(self):
        try:
            # Try converting all non-object columns to Int64
            non_object_cols = self.raw_dataset.select_dtypes(exclude=['object']).columns
            for col in non_object_cols:
                self.raw_dataset[col] = pd.to_numeric(self.raw_dataset[col], errors='coerce').astype('Int64')
            logging.info(f"Successfully converted columns to integer: {list(non_object_cols)}")
        except Exception as e:
            logging.error(f"Error during integer conversion: {e}")

        return self


    def replace_columns(self):
        try:
            self.raw_dataset['Transmission'] = self.raw_dataset['Transmission'].replace({
                'Automatic Transmission': 'Automatic', 
                'Manual Transmission': 'Manual'
            }, inplace=False)
            self.raw_dataset['Cylinders'] = self.raw_dataset['Cylinders'].replace('Unknown', np.nan)
            logging.info("Successfully replaced column values")
        except Exception as e:
            logging.error(f"Failed to replace some column values: {e}")
        return self


    def add_underscore_to_columns(self):
        try:
            self.raw_dataset.columns = ['_'.join(column.split()) for column in self.raw_dataset.columns]
            logging.info("Successfully added underscores to column titles")
        except Exception as e:
            logging.error(f"Failed to add underscores to column titles: {e}")
        return self


    
    def imputate_null_values(self):
        try:
            for column in self.raw_dataset.select_dtypes(include=['float64', 'int64']).columns:
                self.raw_dataset[column] = self.raw_dataset[column].fillna(self.raw_dataset[column].mean())
                logging.info(f"Successfully imputated numerical values for {column}")
        except Exception as e:
            logging.error(f"Failed to imputate some numeric values: {e}")


        try:
            for column in self.raw_dataset.select_dtypes(include=['object']).columns:
                self.raw_dataset[column] = self.raw_dataset[column].fillna(self.raw_dataset[column].mode()[0])
                logging.info(f"Successfully imputated alphabetic values for {column}")
        except Exception as e:
            logging.error(f"Failed to imputate some alphabetic values: {e}")

        return self


    
    def remove_duplicates(self):
        try:
            logging.info(f"Number of rows before removing duplicates: {len(self.raw_dataset)}")
            # Remove duplicate rows based on all columns
            self.raw_dataset = self.raw_dataset.drop_duplicates(keep='first')
            logging.info(f"Number of rows after removing duplicates: {len(self.raw_dataset)}")
        except Exception as e:
            logging.error(f"Failed to remove some duplicate values: {e}")

        return self

    

    def clean_all(self):
        return (
            self.strip_spaces()
                .titlise_columns()
                .convert_to_string()
                .convert_all_possible_to_integer()
                .replace_columns()
                .add_underscore_to_columns()
                .imputate_null_values()
                .remove_duplicates()
                .raw_dataset 
        )

    
    
