import os, string


class listdrives:
   def list_available_drives():
       available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
       return available_drives

if __name__ == '__main__':
#initialisation of class
    list_drives = listdrives
# calling the function with in class
    avail_drivs = list_drives.list_available_drives()
    print(avail_drivs)
