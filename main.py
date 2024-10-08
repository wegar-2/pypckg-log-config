import logging

from pypckg_log_config.module1 import add

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    z = add(12, 3)

    logging.info(f"Result: {z}")

    logger.debug("This is a DEBUG message")
    logger.info("This is an INFO message")
    logger.warning("This is a WARNING message")
    logger.error("This is an ERROR message")
    logger.critical("This is a CRITICAL message")
