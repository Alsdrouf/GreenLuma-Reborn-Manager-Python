import os as os

def Listfile():
    number = 0
    file_list = []
    while str(number)+".txt" in os.listdir():
        file_list.append(str(number)+".txt")
        number+=1
    return file_list

def Listgame():
    appid_list = []
    name_list = []
    isdlc_list = []
    game_list = []
    for file in Listfile():
        f = open(file, "r")
        content=f.readlines()
        appid=content[0]
        appid=appid[0:len(appid)-1]
        name=content[1]
        name=name[0:len(name)-1]
        isdlc=content[2]
        print(appid, name, isdlc)
        appid_list.append(appid)
        name_list.append(name)
        isdlc_list.append(isdlc)
        game_list.append((appid, name, isdlc, file))
        f.close()
    print(appid_list)
    print(name_list)
    print(isdlc_list)
    print(game_list)
    return game_list
