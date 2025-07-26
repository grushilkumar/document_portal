import os
from datetime import datetime
import logging


class CustomLogger:
    def __init__(self, log_dir='logs'):
        self.logs_dir = os.path.join(os.getcwd(), log_dir)
        os.makedirs(self.logs_dir, exist_ok=True)

        log_file = f"{datetime.now().strftime('%m-%d-%Y_%H-%M-%S')}.log"
        log_file_path = os.path.join(self.logs_dir, log_file)

        logging.basicConfig(
            filename=log_file_path,
            level=logging.INFO,
            format='[ %(asctime)s ]- %(levelname)s %(name)s (line:%(lineno)d) - %(message)s',
        )

    def get_logger(self, name = __file__):
        return logging.getLogger(os.path.basename(name))
    
if __name__ == "__main__":
    logger = CustomLogger()
    logger = logger.get_logger(__file__)
    logger.info("Custom logger initialized and ready to use.")
