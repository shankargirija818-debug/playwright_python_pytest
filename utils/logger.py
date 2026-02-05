import logging
import os
from datetime import datetime

class Logger:
    @staticmethod
    def get_logger(name="PlaywrightAutomation"):
        """
        Standardizes logging format for console and file output.
        """
        # Create 'logs' directory if it doesn't exist
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Create a unique log filename based on current date
        log_file = os.path.join(log_dir, f"test_run_{datetime.now().strftime('%Y-%m-%d')}.log")

        logger = logging.getLogger(name)
        
        # Prevent duplicate logs if logger is already configured
        if not logger.handlers:
            logger.setLevel(logging.INFO)

            # Formatting: Timestamp | Level | Class/Method Name | Message
            formatter = logging.Formatter(
                '%(asctime)s - %(levelname)s - [%(name)s] - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )

            # File Handler (Writes logs to a file)
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

            # Console Handler (Prints logs to terminal)
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

        return logger