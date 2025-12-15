import logging
import os

logger = logging.getLogger("omnichat")

def setup_logging():
    log_level = os.getenv("LOG_LEVEL", "INFO")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(log_level)
    
    return logger
