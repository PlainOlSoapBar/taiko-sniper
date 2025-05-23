import logging
import logging.handlers
import os

FILE_PATH = os.path.join(os.path.dirname(__file__), 'run.log')


def setup_logger():
    logger = logging.getLogger("discord")
    logger.setLevel(logging.DEBUG)
    logging.getLogger("discord.http").setLevel(logging.INFO)

    handler = logging.handlers.RotatingFileHandler(
        filename=FILE_PATH,
        encoding="utf-8",
        maxBytes=32 * 1024 * 1024,
        backupCount=5,
    )
    formatter = logging.Formatter(
        "[{asctime}] [{levelname:<8}] {name}: {message}",
        "%Y-%m-%d %H:%M:%S",
        style="{",
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
