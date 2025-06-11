import logging


logging.basicConfig(
    level=logging.INFO,  # Set the minimum log level
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log message format
    # filename='app.log'  # Log to a file (optional)
)



class FeatureEngineering:
    def __init__(self, df):
        self.df = df




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
