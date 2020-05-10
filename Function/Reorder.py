import os as os

def Reorder():
    number = 0
    list_file=[]
    for file in os.listdir():
        if file[len(file)-3:len(file)] == "txt":
            list_file.append(file)
    list_file.sort(key=len)
    for file in list_file:
        if file != str(number)+".txt":
            os.rename(file, str(number)+".txt")
        number+=1
