import plotly.express as px

class Visualisation:
    def bar_chart(self, data, x, y):
        fig = px.bar(data, x=x, y=y)
        fig.show()
