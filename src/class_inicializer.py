import os
import logging
from datetime import datetime

from .graph_generator import GraphGenerator

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
    def __init__(self):
        self.graph_generator_obj: GraphGenerator = GraphGenerator()


class AppContainer:
    def __init__(self):
        self.botcity_container: BotCityContainer = BotCityContainer()
        self.driver_container: DriverContainer = DriverContainer()
        self.graph_container: GraphContainer = GraphContainer()