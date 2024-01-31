import os
import tarfile
import time

filesSimpan = []

def findAndExtract():
    # os.getcwd()
    listdir = os.listdir(os.getcwd())
    # print(listdir)
    defaultDir = os.getcwd()
    for x in listdir:
        if (x == "ftp.py"):
            break
        else:
            os.chdir(defaultDir) # Root directory
            os.chdir(x) # Each of camera
            # print(os.listdir(os.getcwd()))
            listFiles = os.listdir(os.getcwd())
            for i in listFiles:
                # print(i[-3:])
                filename = i+".tar"
                print(filename)
                with tarfile.open(filename, "w") as tar: #name of file
                    tar.add(i)
                filenamepath = os.getcwd()+"\\"+filename
                # print(filenamepath)
                filesSimpan.append(filenamepath)
                # file.write("put " + os.getcwd())
                # file.write(filename)
    # print(files)
                
def createFtp():
    file = open("../ftp.txt", "a")
    file.write("open ftp://xxx:xxx@xxxx \n")
    print(filesSimpan)
    for x in filesSimpan:
        # print(x)
        file.write('put ' + '"' + x + '"' + '\n')
    file.write("exit")
    file.close()

def uploadFiles():
    cmd1 = 'C:\\Users\\xxx\\AppData\\Local\\Programs\\WinSCP\\WinSCP.com /ini=nul /script="../ftp.txt" '
    os.system(cmd1)


def removeFiles():
    # print(os.listdir(os.getcwd()))
    # os.remove("ftp.txt")
    for root, dirs, files in os.walk("../"):
        for file in files:
            if file.endswith(".txt"):
                print(os.path.join(root, file))
                os.remove(os.path.join(root, file))
            if file.endswith(".tar"):
                print(os.path.join(root, file))
                os.remove(os.path.join(root, file))
    
findAndExtract()
createFtp()
uploadFiles()
removeFiles()