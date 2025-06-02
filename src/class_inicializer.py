import os
import logging
from datetime import datetime

import pandas as pd
import plotly.express as px

from botcity.web import WebBot

from rpa_driver_downloader import Gecko  # My own package: https://pypi.org/project/rpa-driver-downloader/


class Logging:
    def __init__(self):
        self._create_logging()


    def _create_logging(self) -> logging:
        log_dir = os.path.join(os.getcwd(), "botcity-fipezap-monitor")
        os.makedirs(log_dir, exist_ok=True)

        today = datetime.now().strftime("%d-%m-%Y")
        LOG_FILE = os.path.join(log_dir, f"log-{today}.txt")

        logging.basicConfig(
            level=logging.info,
            format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            handlers=[
                logging.FileHandler(LOG_FILE, encoding='utf-8')
            ]
        )
        


class BotCityContainer: # Container class that instantiates WebBot from the botcity (web) library
    def __init__(self) -> WebBot:
        self.bot_obj: WebBot = WebBot 


class DriverContainer:  # Container class that instantiates a driver from the rpa_driver_downloader library
    def __init__(self) -> Gecko:
        self.driver_obj: Gecko = Gecko


class GraphContainer:
    
    def __init__(self):
        # No fixed dependencies will be used, constructor just for reuse
        pass


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


class AppContainer:
    def __init__(self):
        self.bot_instance: BotCityContainer = BotCityContainer()
        self.driver_instance: DriverContainer = DriverContainer()
        self.graph_instance: GraphContainer = GraphContainer()