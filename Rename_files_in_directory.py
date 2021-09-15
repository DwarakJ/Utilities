
from dateutil.relativedelta import relativedelta
import datetime
import os

def get_dates():
    result = []

    today = datetime.date(2021, 8, 1) 
    current = datetime.date(2018, 8, 1)    

    while current <= today: #mydate.strftime("%B")
        result.append(str(current.year)+"_"+str(current.strftime("%B")))
        current += relativedelta(months=1)

    return list(reversed(result))

def get_files():

    search_dir = "/Users/djothi/Documents/OptumDocs/Taxsheets/"
    os.chdir(search_dir)
    files = filter(os.path.isfile, os.listdir(search_dir))
    files = [os.path.join(search_dir, f) for f in files] # add path to each file
    files.sort(key=lambda x: os.path.getmtime(x))

    return files

def rename_files(old_file_names, new_file_names):
    
    for i in range(len(old_file_names)):
        os.rename(old_file_names[i], new_file_names[i]+".pdf")

rename_files(get_files(), get_dates())