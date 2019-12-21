import os
import toml
from logging import getLogger
from logging.config import dictConfig


CONFIGFILE = "logging.config.toml"
LOGGERNAME = "root"


def init_logger(configfile, loggername):
    global CONFIGFILE 
    global LOGGERNAME
    CONFIGFILE = configfile
    LOGGERNAME = loggername
    dictConfig(toml.load(CONFIGFILE))
    logger = getLogger(LOGGERNAME)


def get_logger():
    return getLogger(LOGGERNAME)
