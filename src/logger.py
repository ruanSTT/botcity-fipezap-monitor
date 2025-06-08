import os
import logging
from datetime import datetime


class CreateLogging:
    def __init__(self):
        self._create_logging_file()

    
    def _create_logging_file(self):
        current_date = datetime.now().strftime("%m/%d/%Y")
        log_dir = 'bot_logging'

        os.makedirs(log_dir, exist_ok=True)
        log_file_path = os.path.join(log_dir, f'fipe_zap_{current_date}_logging.txt')

        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        logging.basicConfig(
            filename=log_file_path,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%m-%d-%Y %H:%M:%S'
        )
        if os.path.exists(log_file_path):
            return
        else:
            logging.info("The Logging file (.txt) was created.")


class LoggingTitle:
    def __init__(self, full_width=60, character='-'):
        self.full_width = full_width
        self.character = character


    def __getattr__(self, name):
        text = name.replace("_", " ").upper()

        side = (self.full_width - len(text) - 4) // 2
        if side < 0:
            side = 2

        line = f"|{self.character * side} {text} {self.character * side}|"
        return line