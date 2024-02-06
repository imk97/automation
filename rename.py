import os

user = []
def userInput():
    tarikh = input("Nyatakan tarikh yang ingin dibina: ")
    user.append(tarikh)

def createAndRenFile():
    # f = open(user[0]+".tar", "x")
    for x in range(1,31):
        if (x < 10):
            # print("Hello world"+"0"+str(x))
            open(user[0]+"_0"+str(x)+".tar", "x")
        else:
            # print("Hello world"+str(x))
            open(user[0]+"_"+str(x)+".tar", "x")

userInput()
createAndRenFile()