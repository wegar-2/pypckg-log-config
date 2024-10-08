import logging

from pypckg_log_config.module1 import add


if __name__ == "__main__":
    z = add(12, 3)

    logging.info(f"Result: {z}")
