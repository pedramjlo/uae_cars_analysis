import pandas as pd
import numpy as np
import re 
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

    
    def normalise_columns(self):
        try:
            self.raw_dataset.columns = ["_".join(col.lower().split()) for col in self.raw_dataset.columns]
            logging.info("Successfully converted column names")
        except Exception as e:
            logging.error(f"Failed to convert columns: {e}")
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
    

    """
    Extracting condition data from dscription column into a new column based on a regex pattern
    """

    def create_condition_column(self):
        column_name = "condition"

        if "description" in self.raw_dataset.columns:
            if column_name not in self.raw_dataset.columns:
                try:
                    # Match city only if it appears after a comma at the end of the string
                    regex_pattern = r'(?i)condition:\s*(.*)\.'
                    self.raw_dataset[column_name] = self.raw_dataset["description"].str.extract(regex_pattern, flags=re.IGNORECASE)
                    logging.info(f"Extracted city names to column {column_name}.")
                except Exception as e:
                    logging.error(f"Failed to extract the condition: {e}")
            else:
                logging.warning(f"Column {column_name} already exists!")
        else:
            logging.error("Column 'description' does not exist.")

    

    def clean_all(self):
        self.strip_spaces()
        self.normalise_columns()
        self.convert_to_string()
        self.convert_all_possible_to_integer()
        self.replace_columns()
        self.add_underscore_to_columns()
        self.imputate_null_values()
        self.remove_duplicates()
        self.create_condition_column()
        return self.raw_dataset

    
    
