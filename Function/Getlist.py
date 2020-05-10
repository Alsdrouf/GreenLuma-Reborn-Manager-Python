import os as os

def Listfile():
    number = 0
    file_list = []
    while str(number)+".txt" in os.listdir():
        file_list.append(str(number)+".txt")
        number+=1
    return file_list

def ListGame()
