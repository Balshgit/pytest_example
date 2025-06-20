import sys
from logging import Logger


def configure_logger() -> Logger:
    try:
        from loguru import logger as loguru_logger

        loguru_logger.remove()
        loguru_logger.add(
            sink=sys.stdout,
            colorize=True,
            level='DEBUG',
            format='<cyan>{time:DD.MM.YYYY HH:mm:ss}</cyan> | <level>{level}</level> | <magenta>{message}</magenta>',
        )
        return loguru_logger  # type: ignore
    except ImportError:
        import logging

        logging_logger = logging.getLogger('main_logger')
        formatter = logging.Formatter(
            datefmt='%Y.%m.%d %H:%M:%S',
            fmt='%(asctime)s | %(levelname)s | func name: %(funcName)s | message: %(message)s',
        )
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)
        logging_logger.setLevel(logging.INFO)
        logging_logger.addHandler(handler)
        return logging_logger


logger = configure_logger()
