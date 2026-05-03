import logging
import os

#logger setup paste from ai
def setup_logger():
    os.makedirs("./logs", exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logging.getLogger("httpx").setLevel(logging.WARNING)

    log_format = logging.Formatter(
            fmt='[%(asctime)s] %(levelname)s(%(funcName)s): %(message)s',
            datefmt='%d-%m-%y %H:%M:%S')

    file_h = logging.FileHandler("./logs/bot.log")
    file_h.setFormatter(log_format)

    console_h = logging.StreamHandler()
    console_h.setFormatter(log_format)

    logger.addHandler(file_h)
    logger.addHandler(console_h)
