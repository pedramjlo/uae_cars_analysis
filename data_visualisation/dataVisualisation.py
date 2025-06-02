import plotly.express as px

class Visualisation:

    def bar_chart(self, data, x, y, title=None, labels=None):
        fig = px.bar(data, x=x, y=y, title=title, labels=labels)
        fig.update_traces(marker_color='purple')
        fig.update_yaxes(type="log")
        fig.show()


    def line_chart(self, data, x, y, title=None, labels=None, color=None):
        fig = px.line(data, x=x, y=y, title=title, labels=labels, color=color)
        fig.update_traces(marker_color='purple')
        fig.show()

    def pie_chart(self, data, x, y, title=None, labels=None):
        fig = px.scatter(data, x=x, y=y, title=title, labels=labels)
        fig.show()

    def box_plot(self, data, x, y, title=None, labels=None):
        fig = px.box(data, x=x, y=y, title=title, labels=labels)
        fig.update_yaxes(type="log")
        fig.show()
