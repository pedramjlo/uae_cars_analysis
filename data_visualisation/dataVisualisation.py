import plotly.express as px

class Visualisation:
    def __init__(self, df):
        self.df = df

    def bar_chart(self, x, y):
        fig = px.bar(self.df, x='year', y='pop')
        fig.show()
