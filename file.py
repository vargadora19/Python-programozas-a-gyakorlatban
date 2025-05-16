class Date:
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.year}-{self.month}-{self.day}"

    def year_check(self, year: int):
        return year == self.year

    def month_check(self, month: int):
        return month == self.month

    def day_check(self, day: int):
        return day == self.day

    def string(self):
        year = self.year
        if len(self.month.__str__()) == 1:
            month = "0" + self.month.__str__()
        else:
            month = self.month.__str__()

        if len(self.day.__str__()) == 1:
            day = "0" + self.day.__str__()
        else:
            day = self.day.__str__()
        # print(f"{year}{month}{day}")
        return f"{year}{month}{day}"

    def between(self, date_low:['Date']=None, date_high:['Date']=None)->bool:
        if date_low is None and date_high is None:
            return True
        elif date_low is None and date_high is not None and self.string()<=date_high.string():
            return True
        elif date_high is None and date_low is not None and self.string()>=date_low.string():
            return True
        elif date_high is not None and date_low is not None and date_high.string() >= self.string() >= date_low.string():
            return True
        else:
            return False


class File:
    def __init__(self,date:Date, name:str, extension:str):
        self.date = date
        self.name = name
        self.extension = extension

    def __str__(self):
        return self.date.__str__() + " " + self.name + " " + self.extension


class Folder:
    def __init__(self,name:str):
        self.folder_name = name.split(" ")[0]
        self.count = name.split(" ")[1]
    def __str__(self):
        return self.folder_name + " _ " + self.count
