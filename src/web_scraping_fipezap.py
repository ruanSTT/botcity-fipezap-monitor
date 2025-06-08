import pandas as pd

from .class_inicializer import GraphContainer

from botcity.web import WebBot
from rpa_driver_downloader import Gecko


class FipeZapMain():
    def __init__(self,
                 webbot: WebBot,
                 driver: Gecko,
                 graph_container: GraphContainer
        ):
        self.bot: WebBot = webbot
        self.driver: Gecko = driver
        self.graph: GraphContainer = graph_container