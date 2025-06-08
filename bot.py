from src.class_inicializer import AppContainer
from src.web_scraping_fipezap import FipeZapMain

class InicializeProcess:
    """
    The class that starts all the automation process.
    """
    def __init__(self):
        container: AppContainer = AppContainer()

        FipeZapMain(
            webbot=container.botcity_container.webbot_obj,
            driver=container.driver_container.driver_obj,
            graph_container=container.graph_container
        )
        
