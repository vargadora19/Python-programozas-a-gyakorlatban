import os
import shutil
from file import File, Folder

def copy(from_path:str, to_path:str):
    shutil.copy(from_path, to_path)

def files_copy(files:list[File], to_path:str, downloads:str, required_list=None):
    if required_list is None:
        required_list = []
    folders=os.listdir(to_path)
    folders_list=[]
    for folder in folders:
        folders_list.append(Folder(folder))
    for folder in folders_list:
        print(folder)

    for file in files:
        for folder in folders_list:
            if file.extension == folder.folder_name and (required_list[0]=='' or file.extension in required_list):
                copy(os.path.join(downloads, file.name), os.path.join(to_path, folder.folder_name + " " + folder.count))

    print("--------------------------------------------------------")
    for f in files:
        print(f)
    print(files, "fc: "+to_path, downloads, required_list)