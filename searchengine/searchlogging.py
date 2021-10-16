import logging

def log_creation():
    # Gets or creates a logger
    logger = logging.getLogger(__name__)
    # set log level
    logger.setLevel(logging.DEBUG)
    # define file handler and set formatter
    file_handler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
    file_handler.setFormatter(formatter)
    # add file handler to logger
    logger.addHandler(file_handler)
    return logger

if __name__ == '__main__':
# Call the log_creation function from the searchlogging script for logging purpose
    logger = log_creation()
    logger.info("Logging is enabled")
