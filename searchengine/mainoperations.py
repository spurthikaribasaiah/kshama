import threading
import listdirectories as ld
import searchlogging as sl
import searchdirectories as sd

class main_operations:
    def main_opers(logger):
        try:
            logger.info("Running the main script")

            # Call the list_available_drives function from listdirectories script to print the list of available directories
            # Initialisation of class
            list_drives = ld.listdrives
            # Calling the function
            avail_drivs = list_drives.list_available_drives()
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

            # Take the user input to search in the specific directory
            print("Please input the directory name to search for the file : ")
            dir_names = input()

            # Creating the list of files from the input
            file_list = file_names.split(',')
            logger.info("Search engine will be searching the files mentioned in parallel: " + str(file_list))

            # Creating the list of directories from the input
            if dir_names is not None or dir_names != '':
                dir_list = dir_names.split(',')
            else:
                dir_list = avail_drivs

            logger.info(
                "Search engine will be searching the files mentioned in parallel in the mentioned directories: " + str(
                    dir_list))

            # Creating threads to run in multithread and call search_file_in_drives function from searchdirectories script to search in the history and then search in the drives
            # Initialisation of class
            searchdrvs = sd.search_drives
            # Calling the function in multi threading
            threads = []
            for file_name in file_list:
                t = threading.Thread(target=searchdrvs.search_file_in_drives, args=[file_name, dir_list, logger])
                t.start()
                threads.append(t)
                logger.info(f'Active Threads: {threading.active_count()}')
            for thread in threads:
                thread.join()

            status = 'Success'
            error = 'NA'

        except Exception as strerror:
            logger.exception(strerror)
            status = 'Failed'
            error = strerror

        return status,error


if __name__ == '__main__':
    # Call the log_creation function from the searchlogging script for logging purpose
    # Initialisation of class
    seach_log = sl.search_logging
    # Calling the function
    logger = seach_log.log_creation()
    stats,err = main_operations.main_opers(logger)
    print(stats,err)
