import logging


logger = logging.getLogger(__name__)


def add(x, y):
    logger.info(f"Adding {x=} and {y=}")
    return x + y
