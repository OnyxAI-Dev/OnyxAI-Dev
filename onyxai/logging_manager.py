import logging
from config.settings import LOG_FILE, LOG_FORMAT

def setup_logger(name):
    """
    Set up a logger with the specified name.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler(LOG_FILE)
    formatter = logging.Formatter(LOG_FORMAT)
    handler.setFormatter(formatter)

    if not logger.hasHandlers():
        logger.addHandler(handler)
    return logger
