import Getlist as getlist
import Reorder as reorder
import os as os

def Removebyname(name=""):
    game_list = getlist.Listgame()
    for game in game_list:
        if game[1] == name:
            print("Removing : ", game[3])
            os.remove(game[3])
    reorder.Reorder()

def Removebyappid(appid=""):
    game_list = getlist.Listgame()
    for game in game_list:
        if game[0] == appid:
            print("Removing : ", game[3])
            os.remove(game[3])
    reorder.Reorder()
