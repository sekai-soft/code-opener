import logging
from logging.handlers import RotatingFileHandler

"""
Create a logger and set the logging level,
then create a formatter for the handlers
"""
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a file handler
log_file = 'code-opener.log'
file_handler = RotatingFileHandler(log_file, maxBytes=100000, backupCount=5)

# Create a stream handler for stdout
# stream_handler = logging.StreamHandler(sys.stdout)
stream_handler = None 

"""
Set logging level and formatter for the file_handler,
then add the file_handler to the logger
"""
file_handler.setLevel(logging.DEBUG)  
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

if stream_handler is not None:
    # the same as above
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
