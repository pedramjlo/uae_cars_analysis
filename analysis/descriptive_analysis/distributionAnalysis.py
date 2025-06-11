from scipy.stats import skew


class Distribution:
    def __init__(self, df, plot):
        self.df = df
        self.plot = plot



    def get_std(self, group_by_col: str, target_col: str):

        """
        applying standard deviation for each make's price => std per make
        """

        try:
            std_per_group = (
                self.df.groupby(group_by_col)[target_col]
                .apply(lambda x: x.std())
                .reset_index()
            )

            self.plot.scatter_plot(
                data=std_per_group,
                x=group_by_col,
                y=target_col,
                title=f"Standard Deviation of {target_col} across {group_by_col}s"
            )
            return std_per_group
        except Exception as e:
            raise e
            



from scipy.stats import skew

class Skewness:
    def __init__(self, df, plot):
        self.df = df
        self.plot = plot

    def get_skewness(self, group_by_col, target_col):
        """
        Calculate skewness of target_col grouped by group_by_col.

        Args:
            group_by_col (str): Column name to group by (e.g., 'make').
            target_col (str): Numeric column to calculate skewness (e.g., 'price').

        Returns:
            pd.DataFrame: DataFrame with group_by_col and skewness values.
        """
        try:
            skewness_per_group = (
                self.df.groupby(group_by_col)[target_col]
                .apply(lambda x: skew(x.dropna()))
                .reset_index()
            )
            skewness_per_group = skewness_per_group.rename(columns={target_col: f"{target_col}_skewness"})
            skewness_per_group = skewness_per_group.sort_values(by=f"{target_col}_skewness")
            return skewness_per_group
        except Exception as e:
            raise e
