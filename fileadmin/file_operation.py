import os

class FileOperator:

    def __init__(self):
        pass

    def create_file(self, dir, filename):
        result = os.system('touch {d}/{f_n}'.format(d=dir, f_n=filename))
    
    def move(self, path, tar_path):
        result = os.system('mv {p} {t_p}'.format(p=path, t_p=tar_path))
        
    def rename(self, path, new_name):
        self.move(path=path, tar_path=new_name)

    def remove(self, path):
        try:
            os.remove(path)
        except OSError:
            try:
                os.rmdir(path)
            except OSError:
                os.system('rm -rf {p}/*'.format(p=path))
                os.rmdir(path)

    def copy(self, path, tar_path):
        os.system('cp {p} {t_p}'.format(p=path, t_p=tar_path))

if __name__ == "__main__":
    path = os.getcwd() + "/getProperties.py"
    fo = FileOperator()
    fo.remove(os.getcwd()+"/new2.py")
