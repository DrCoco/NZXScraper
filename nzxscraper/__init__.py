from os import path, remove
import logging
import logging.config
import json

# If applicable, delete the existing log file to generate a fresh log file during each execution
if path.isfile("python_logging.log"):
    remove("python_logging.log")

with open("python_logging_configuration.json", 'r') as logging_configuration_file:
    config_dict = json.load(logging_configuration_file)

logging.config.dictConfig(config_dict)

# Log that the logger was configured
logger = logging.getLogger(__name__)
logging.getLogger("selenium").setLevel(logging.WARNING)
logger.info('Completed configuring logger()!')