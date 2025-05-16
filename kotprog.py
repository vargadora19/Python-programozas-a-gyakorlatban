from datetime import datetime
from copyfiles import *

from file import File,Date

files=[]
def list_downloads(path: str, start_date:Date=None, end_date:Date=None):
    global files
    os.chdir(path)
    for filename in os.listdir(path):
        full_path = os.path.join(path, filename)
        if os.path.isfile(full_path):
            modified_time = os.path.getmtime(full_path)
            date = datetime.fromtimestamp(modified_time)
            file = File(Date(date.year, date.month, date.day), filename, filename.split('.')[-1])
            if file.date.between(start_date, end_date):
                files.append(file)
    print("ld: "+path, start_date, end_date)

def create_clean_folder(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)

def folder_maker(path:str, required_list=None):
    global files
    for i in files:
        print(i)

    dikt=dict()
    # for i in files:
    #     print(i,"   @ " + i.extension)
    for f in files:
        if required_list is None or required_list[0]=='' or f.extension in required_list :
            dikt[f.extension] = dikt.get(f.extension,0) + 1
    os.chdir(path)
    for key,value in dikt.items():
        # os.mkdir(path=key + "(" + str(value) + ")")
        create_clean_folder(key + " (" + str(value) + ")")
    mappak=os.listdir(".")
    for i in mappak:
        print(i)

    print(os.getcwd())
    print("fm: "+path, required_list)

# if __name__ == "__main__":
    # required_extensions=["pdf", "docx", "jpg"]
    # date_low=Date(2025,1,2)
    # date_high=Date(2025, 4, 7)
    # date3=Date(2025, 8,3)
    # date4=Date(2024, 12,20)
    # valami=date2.between()
    # print(valami)
    # list_downloads(r"C:\Users\Asus\Downloads", start_date= date_high)
    # folder_maker(r"C:\Users\Asus\Desktop\egyetem\4.felev\python_mappak")
    # files_copy(files,r"C:\Users\Asus\Desktop\egyetem\4.felev\python_mappak", r"C:\Users\Asus\Downloads")