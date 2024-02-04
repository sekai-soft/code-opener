import logging
from logging.handlers import RotatingFileHandler

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Set the logging level

# Create a file handler
log_file = 'code-opener.log'
file_handler = RotatingFileHandler(log_file, maxBytes=100000, backupCount=5)
file_handler.setLevel(logging.DEBUG)  # Set the logging level for the file

# Create a stream handler for stdout
# stream_handler = logging.StreamHandler()
# stream_handler.setLevel(logging.DEBUG)  # Set the logging level for stdout

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Set the formatter for the handlers
file_handler.setFormatter(formatter)
# stream_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
# logger.addHandler(stream_handler)
