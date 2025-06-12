import logging
import re


logging.basicConfig(
    level=logging.INFO,  # Set the minimum log level
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log message format
    # filename='app.log'  # Log to a file (optional)
)




class FeatureEngineering:
    def __init__(self, df):
        self.df = df


    """
    Extracting condition data from dscription column into a new column based on a regex pattern <condition: .>
    """
    def create_condition_column(self):
        column_name = "condition"

        if "description" in self.df.columns:
            if column_name not in self.df.columns:
                try:
                    # Pattern to extract condition
                    regex_pattern = r'(?i)condition:\s*(.*?)\.'

                    # Extract condition to new column
                    self.df[column_name] = self.df["description"].str.extract(regex_pattern, flags=re.IGNORECASE)

                    # Remove the condition part from the description
                    self.df["description"] = self.df["description"].str.replace(regex_pattern, '', flags=re.IGNORECASE, regex=True).str.strip()

                    logging.info(f"Extracted condition values to column '{column_name}' and removed them from description.")
                except Exception as e:
                    logging.error(f"Failed to extract the condition: {e}")
            else:
                logging.warning(f"Column '{column_name}' already exists!")
        else:
            logging.error("Column 'description' does not exist.")



    def run_feature_engineering(self):
        self.create_condition_column()
        return self.df

    

