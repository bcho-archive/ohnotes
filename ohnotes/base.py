#coding: utf-8

import logging

from utils import register_logger
from config import log_level, log_path, log_format, log_name

#: init logger

logger = logging.getLogger(log_name)
logger.setLevel(log_level)
formatter = logging.Formatter(log_format)

file_handler = logging.FileHandler(log_path)
console_handler = logging.StreamHandler()

for handler in [file_handler, console_handler]:
    register_logger(handler, log_level, formatter)
    logger.addHandler(handler)
