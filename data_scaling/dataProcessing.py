"""
processing the skewness, standard deviation, and median prices for data scaling
"""

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
