import os, string


def list_available_drives():
    available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
    return available_drives

if __name__ == '__main__':
    avail_drivs = list_available_drives()
    print(avail_drivs)
