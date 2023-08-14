import logging
# filename:
import datetime as dt
today = dt.datetime.today()
filename = f"{today.day:02d}-{today.month:02d}-{today.year}.log"

# 5 levels:
""" debug
info
Warning
error
critical
 """
# change logging level
logging.basicConfig(level=logging.DEBUG)
# if due to some reason basicconfig() doesnt work use:


# by default logger is root, if you want to change then:
logger = logging.getLogger("Rayan")


# File Handler:Add logging messages into files:
file_handler = logging.FileHandler(f"/home/rayan/Documents/Python/logging_module/{filename}") # filename according to date(in the beginning)
file_handler.setLevel(logging.WARNING) # warning and everything above appears in logfile

#formatting for logging messages into files:
formatter = logging.Formatter("%(asctime)s - %(levelname)s : %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.debug("Hi i am debug")
logger.info("Hi i am info")
logger.warning("Hi i am warning")
logger.error("Hi i am error")
logger.critical("Hi i am critical")


