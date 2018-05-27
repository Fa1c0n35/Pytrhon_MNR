import logging

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s' \
,datefmt="%d/%m/%Y %H:%M:%S")

logger = logging.getLogger("Logger")
logger.setLevel(logging.DEBUG)

# create a file handler
handler = logging.FileHandler('testlog.log')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

logger.debug("Message01")
logger.info("Message02")
logger.warning("Message03")
logger.error("Message04")
logger.critical("Message05")

logger.removeHandler(handler)

