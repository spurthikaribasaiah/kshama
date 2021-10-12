import os, string

class drivesearch:
    def list_available_drives(self):
       available_drives = ['%s:' % d for d in string.ascii_lowercase if os.path.exists('%s:' % d)]
       return available_drives

    def search_file_in_drives(self, filename, directorylist = None):
        filelist = []
        # if statement to check if the specific directory is passed else search in all the directories.
        if directorylist is None or directorylist == '':
            dirlist = self.list_available_drives()
        else:
            dirlist = directorylist.split(',')
        print(dirlist)

        # search for the file in the directories
        for dirname in dirlist:
            dirname = dirname if ':' in dirname else dirname + ':'
            print(dirname)
            for dirpath, dirs, files in os.walk(dirname):
                for file in files:
                    if filename in file:
                        filelist.append(os.path.join(dirpath, file))

        return filelist

if __name__ == "__main__":
    print("welcome to the file search engine")

    # Initialisation of the class
    drv_srch = drivesearch()

    # calling the function to list the available drives on the computer
    avail_drivs = drv_srch.list_available_drives()
    print(avail_drivs)

    # Taking the user input to select the directory to search for the file and the specific file name to search
    file_name = input("File Name is mandatory to put. Please input the file name to search for : ")
    directory_name = input("please select the directories to search from the above list mentioned eg:('c:','c:,h:') : ")

    # Search for the mentioned file in the directory.
    filelst = drv_srch.search_file_in_drives(file_name, directory_name)
    print(filelst)
