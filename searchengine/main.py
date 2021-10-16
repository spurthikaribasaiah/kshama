import threading
import listdirectories as ld
import searchlogging as sl
import searchdirectories as sd


if __name__ == '__main__':
    try:
# Call the log_creation function from the searchlogging script for logging purpose
        logger = sl.log_creation()
        logger.info("Welcome to the file search engine")

# Call the list_available_drives function from listdirectories script to print the list of available directories
        avail_drivs = ld.list_available_drives()
        logger.info("the list of available directories are: " + str(avail_drivs))

# Take the user input for the file name to search
        cnt = 1
        file_names = ''
        while cnt < 4 and (file_names is None or file_names == ''):
              print(str(cnt) + " try")
              print("File Name is mandatory to put. Please input the file name to search for : ")
              file_names = input()
              cnt = cnt + 1
        if file_names is None or file_names == '':
              raise Exception("File Name to search is not provided in 3 attempts. Hence aborting the process")

# Creating the list of files from the input
        file_list = file_names.split(',')
        logger.info("Search engine will be searching the files mentioned in parallel: " + str(file_list))

# Creating threads to run in multithread and call search_file_in_drives function from searchdirectories script to search in the history and then search in the drives
        threads = []
        for file_name in file_list:
            t = threading.Thread(target=sd.search_file_in_drives, args=[file_name, avail_drivs, logger])
            t.start()
            threads.append(t)
            logger.info(f'Active Threads: {threading.active_count()}')
        for thread in threads:
            thread.join()

    except Exception as strerror:
        logger.exception(strerror)
        raise
