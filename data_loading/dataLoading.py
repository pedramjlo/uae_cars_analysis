import pandas as pd
import logging


logging.basicConfig(
    level=logging.INFO,  # Set the minimum log level
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log message format
    # filename='app.log'  # Log to a file (optional)
)


class DataLoader:
    def __init__(self, raw_dataset):
        self.raw_dataset = raw_dataset


    def read_data(self):
        """
        handling file existence, empty dataset, and parsing errors
        """
        try:
            logging.info("read the dataset successfully")
            return pd.read_csv(self.raw_dataset, encoding="ISO-8859-1", engine='python')
        except FileNotFoundError:
            logging.error("Error: The file was not found.")
        except pd.errors.EmptyDataError:
            logging.error("Error: The file is empty.")
        except pd.errors.ParserError:
            logging.error("Error: The file could not be parsed.")