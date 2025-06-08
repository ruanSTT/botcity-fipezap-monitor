import os
import logging

from .logger import CreateLogging, LoggingTitle
from .graph_generator import GraphGenerator

from botcity.web import WebBot

from rpa_driver_downloader import Gecko  # My own package: https://pypi.org/project/rpa-driver-downloader/


class LoggingContainer:
    """
    Container that creates a local 'bot_logging' folder, and a logging file (.txt) to follow the process.
    Also create a 'logging_title' object that allows to use customizable logs name.
    """
    def __init__(self):
        self.logger: CreateLogging = CreateLogging()
        self.logger._create_logging_file()

        self.logging_title: LoggingTitle = LoggingTitle()
        
 
class BotCityContainer: 
    """
    Container class that instantiates WebBot from the botcity (web) library.
    """ 
    def __init__(self) -> WebBot:
        self.webbot_obj: WebBot = WebBot 


class DriverContainer:
    """
    Container class that instantiates a driver from the rpa_driver_downloader library
    """
    def __init__(self) -> Gecko:
        self.driver_obj: Gecko = Gecko


class GraphContainer:
    """
    Container class that instantiates a 'graph_generator_obj' object from the GraphGenerator
    """
    def __init__(self):
        self.graph_generator_obj: GraphGenerator = GraphGenerator()


class AppContainer:
    def __init__(self):
        self.botcity_container: BotCityContainer = BotCityContainer()
        self.driver_container: DriverContainer = DriverContainer()
        self.graph_container: GraphContainer = GraphContainer()