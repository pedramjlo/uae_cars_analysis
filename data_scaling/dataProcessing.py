"""
processing the skewness, standard deviation, and median prices for data scaling
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

class DataScaler:
    def __init__(self, strategy="standard"):
        self.strategy = strategy
        self.scaler = None

        if strategy == "standard":
            self.scaler = StandardScaler()
        elif strategy == "minmax":
            self.scaler = MinMaxScaler()
        elif strategy == "robust":
            self.scaler = RobustScaler()
        else:
            raise ValueError(f"Unknown scaling strategy: {strategy}")

    def fit(self, data):
        """
        Fit the scaler to the data.

        Parameters:
        - X: pandas DataFrame or NumPy array with numeric values to scale.

        This method learns the scaling parameters (e.g., mean, std, min, max).
        """
        if self.scaler is None:
            raise RuntimeError("Scaler not initialized properly.")

        self.scaler.fit(data)

    def transform(self, data):
        """
        Transform the data using the fitted scaler.

        Parameters:
        - X: pandas DataFrame or NumPy array (should match shape of data used in fit())

        Returns:
        - pandas DataFrame with scaled values (if X is DataFrame)
        """
        if self.scaler is None:
            raise RuntimeError("Scaler has not been initialized.")
        
        scaled_array = self.scaler.transform(data)
        
        # If input was a DataFrame, return a DataFrame with same columns
        if isinstance(data, pd.DataFrame):
            return pd.DataFrame(scaled_array, columns=data.columns, index=data.index)
        else:
            return scaled_array

