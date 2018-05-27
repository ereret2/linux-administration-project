import os
import stat
from pwd import getpwuid
import time

#Author: Zhu Botong
#tested under WSL(Ubuntu 18.04)

def getCurrentPath():
    return os.getcwd()

def getFilePermission_oct(path):
    #
    return oct(os.stat(path).st_mode & 0o777)

def getFilePermission_str(path):
    #it should look like this : drwxrwxrwx
    permission = ""
    mode = os.stat(path).st_mode
    if stat.S_ISDIR(mode):
        permission = permission + "d"
    else:
        permission = permission + "-"
    if bool(mode & stat.S_IRUSR):
        permission = permission + "r"
    else:
        permission = permission + "-"
    if bool(mode & stat.S_IWUSR):
        permission = permission + "w"
    else:
        permission = permission + "-"
    if bool(mode & stat.S_IXUSR):
        permission = permission + "x"
    else:
        permission = permission + "-"
    if bool(mode & stat.S_IRGRP):
        permission = permission + "r"
    else:
        permission = permission + "-"
    if bool(mode & stat.S_IWGRP):
        permission = permission + "w"
    else:
        permission = permission + "-"
    if bool(mode & stat.S_IXGRP):
        permission = permission + "x"
    else:
        permission = permission + "-"
    if bool(mode & stat.S_IROTH):
        permission = permission + "r"
    else:
        permission = permission + "-"
    if bool(mode & stat.S_IWOTH):
        permission = permission + "w"
    else:
        permission = permission + "-"
    if bool(mode & stat.S_IXOTH):
        permission = permission + "x"
    else:
        permission = permission + "-"
    return permission

def getFileOwner(path):
    return getpwuid(os.stat(path).st_uid).pw_name

def getFileModifiedTime(path):
    return time.ctime(os.stat(path).st_mtime)

def getFileCreatedTime(path):
    return time.ctime(os.stat(path).st_ctime)

if __name__ == "__main__":
    path = os.getcwd() + "/getProperties.py"
    print(getFilePermission_str(os.getcwd()))
    print(os.stat(path))
    print(getFileOwner(path))
    print(getFileModifiedTime(path))