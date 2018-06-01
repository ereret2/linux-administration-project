import os
def createDict(dict_name_path):
    path=os.getcwd()
    dict_name_path_abs=os.path.join(path,dict_name_path)
    if(os.path.exists(dict_name_path)):
        print('The dictory has been created already')
    else:
        os.mkdir(dict_name_path_abs)
if __name__ == "__main__":
    createDict('test')
