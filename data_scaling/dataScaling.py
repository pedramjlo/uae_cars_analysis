from sklearn.preprocessing import StandardScaler


class DataScaler:
    def __init__(self, df, method):
        """
        Args:
            method (str): Scaling strategy. Supported: 
                - "standard"     → zero mean, unit variance 
                - "minmax"       → rescale to [0,1]
                - "robust"       → use IQR for scaling (less sensitive to outliers)
        """
        self.df = df
        self.method = method
        self.scaler = None