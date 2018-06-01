import os
class Directory:
    def __init__(self,dir_path):
        self.dir_path=dir_path
        self.createDir()
    #传入文件夹名，如果该文件夹不存在，则创建
    def createDir(self):
        if(os.path.exists(self.dir_path)==False):
            os.mkdir(self.dir_path)
        else:
            print('The directory has been create already')
    #返回该文件夹下的所有文件和子目录
    def listFile(self):
        return os.listdir(self.dir_path)
    #删除文件夹下名为filename的文件
    def deleteFile(self,filename):
        file_path=os.path.join(self.dir_path,filename)
        if(os.path.exists(file_path)==False):
            print('file is not existed')
        else:
            os.remove(file_path)
    #返回文件夹下面文件个数
    def fileNumber(self):
        return len(os.listdir(self.dir_path))
    #在该文件夹上创建文件
    def createFile(self,filename):
        file_path=os.path.join(self.dir_path,filename)
        if(os.path.exists(file_path)==True):
            print('The file has been created already')
        else:
            os.mknod(filename)
    #删除文件夹
    def deleteDir(self):
        os.removedirs(self.dir_path)
dir=Directory('/Users/liujiaheng/Code/linux-administration-project/directoryAdmin/s')

print(dir.listFile())

print(dir.fileNumber())
dir.deleteDir()




