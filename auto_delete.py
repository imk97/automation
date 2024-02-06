import os
import datetime

def rmPrevData():
    date = datetime.datetime.now()
    cday = date.strftime("%d")
    cmonth = date.strftime("%m")
    cyear = date.strftime("%Y")
    # print(os.listdir(os.getcwd()))
    defaultDir = os.listdir(os.getcwd())
    for a in defaultDir:
        fyear = a[4:8]
        fmonth = a[2:4]
        fday = a[0:2]
        if (a == "auto_delete.py"):
            break
        if (int(fyear) == int(cyear)): # Check year is same or not
            if (int(fmonth) == int(cmonth)): # Check month is same or not
                balance = int(cday) - int(fday)
                if (balance > 0):
                    print(a)
                    os.remove(a)
            if (int(fmonth) < int(cmonth)): # File month less than or not
                print(a)
                os.remove(a)

rmPrevData()