


class Distribution:
    def __init__(self, df, plot):
        self.df = df
        self.plot = plot


    def calculate_std(self, group_by_col, target_col):
        try:
            if group_by_col in self.df.columns and target_col in self.df.columns:
                results = (
                    self.df.groupby(group_by_col)[target_col]
                    .std()
                    .reset_index()
                    .rename(columns={target_col: f"{target_col}_std"})
                )

                self.plot.scatter_plot(
                    data=results,
                    x=group_by_col,
                    y=f"{target_col}_std",
                    title=f"Standard Deviation"
                )
                return results
        except Exception as e:
            raise e
            