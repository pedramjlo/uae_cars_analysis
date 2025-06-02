import plotly.express as px

class Visualisation:

    def bar_chart(self, data, x, y, title=None, labels=None):
        fig = px.bar(data, x=x, y=y, title=title, labels=labels)
        fig.update_traces(marker_color='purple')
        fig.show()


    def line_chart(self, data, x, y, title=None, labels=None):
        fig = px.line(data, x=x, y=y, title=title, labels=labels)
        fig.update_traces(marker_color='purple')
        fig.show()
