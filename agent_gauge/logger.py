# agent_gauge/logger.py

import logging

class Logger:
    def __init__(self):
        logging.basicConfig(
            filename='agent_gauge.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger()

    def log(self, message: str):
        print(message)
        self.logger.info(message)
