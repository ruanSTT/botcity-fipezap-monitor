import pandas as pd
import plotly.express as px


class GraphGenerator:

    def generate_graph(
        self,
        df: pd.DataFrame,
        chart_type: str,
        x_axis: str,
        y_axis: str,
        title: str = "Generated Chart"
    ):
        if chart_type == "line":
            fig = px.line(df, x=x_axis, y=y_axis, title=title)
        elif chart_type == "bar":
            fig = px.bar(df, x=x_axis, y=y_axis, title=title)
        elif chart_type == "scatter":
            fig = px.scatter(df, x=x_axis, y=y_axis, title=title)
        else:
            raise ValueError(f"Unsupported chart type: {chart_type}")

        fig.show()