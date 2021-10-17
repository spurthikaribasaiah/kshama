import searchlogging as sl
import mainoperations as mo


if __name__ == '__main__':
    try:
    # Call the log_creation function from the searchlogging script for logging purpose
    # Initialisation of class
      search_log = sl.search_logging
    # Calling the function
      logger = search_log.log_creation()
      logger.info("Welcome to the file search engine")

    # Call the main operations function from the mainoperations script
    # Initialisation of the class
      mainoper = mo.main_operations
      stats,err = mainoper.main_opers(logger)
      if stats == 'Success':
          logger.info("Search engine successfully completed searching for files in drives")
      else:
          raise Exception("Search engine failed searching for files in drives")

    except Exception as strerror:
        logger.exception(strerror)
        raise
