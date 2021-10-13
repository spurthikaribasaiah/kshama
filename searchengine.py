import os, string
from colorama import init
from colorama import Fore as F
from colorama import Back as B
from colorama import Style
import threading
import time

def color(text, fore='', back=''):
    return f'{fore}{back}{text}{Style.RESET_ALL}'

class drivesearch:
    def list_available_drives(self):
       available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
       return available_drives

    def search_file_in_drives(self, filename, dirname):
        filelist = []
        # search for the file in the directories
        dirname = dirname.upper() if ':' in dirname else dirname.upper() + ':'
        for dirpath, dirs, files in os.walk(dirname):
            for file in files:
                if filename in os.path.join(dirpath, file):
                    filelist.append(os.path.join(dirpath, file))

        if not filelist:
           print(color("There are no files present with the name '" + filename + "' in the directory " + dirname, F.RED))
        else:
           print(color("Please find below the list of search results for the file '" + file_name + "' in the directory " + dirname, F.RED))
           print(color(filelist, F.GREEN))

        return filelist

if __name__ == "__main__":
  try:
      print(color("Welcome to the file search engine", F.BLUE))

    # Initialisation of the class
      drv_srch = drivesearch()

    # Taking the user input to select the directory to search for the file and the specific file name to search
      cnt = 1
      file_name = ''
      while cnt < 4 and (file_name is None or file_name == ''):
            print(str(cnt) + " try")
            print(color("File Name is mandatory to put. Please input the file name to search for : ", F.RED))
            file_name = input()
            cnt = cnt + 1
      if file_name is None or file_name == '':
          raise Exception("File Name to search is not provided in 3 attempts. Hence aborting the process")

    # calling the function to list the available drives on the computer
      avail_drivs = drv_srch.list_available_drives()
      print(color("Please find the list of available directories:", F.RED))
      print(color(avail_drivs, F.GREEN))
      print(color("please select the directories to search from the above list mentioned eg:('C','C,H') : ", F.RED))
      directory_name = input()

    # if statement to check if the specific directory is passed else search in all the directories.
      if directory_name is None or directory_name == '':
          dirlist = drv_srch.list_available_drives()
      else:
          dirlist = directory_name.split(',')

    # Creating threads to run in multithread
      threads = []
      for dirname in dirlist:
          t = threading.Thread(target=drv_srch.search_file_in_drives, args=[file_name,dirname])
          t.start()
          threads.append(t)
      print(f'Active Threads: {threading.active_count()}')
      print(threads)

      for thread in threads:
          thread.join()


  except Exception as strerror:
      print(color(strerror, F.BLUE))
