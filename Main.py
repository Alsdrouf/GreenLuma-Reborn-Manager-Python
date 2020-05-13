#Importing
import sys
import os
import configparser as config
sys.path.append('./Function')
import AddingFile as add
import Reorder as reorder
import Option as option
import Getlist as getlist
import RemovingFile as remove
sys.path.append('../')

config = config.ConfigParser()
config.read('settings.ini')
workpath = config['GENERAL']['Workpath']
os.chdir(workpath)
workpath = os.getcwd()
print(workpath)

#for loop in range(10):
#    numberoffile=len(getlist.Listfile())
#    print(getlist.Listfile())
#    add.Adding(number=numberoffile, name="Benzema", appid=50)
#numberoffile=len(getlist.Listfile())
#add.Adding(number=numberoffile, name="Benzema", appid=50)
#reorder.Reorder()
#getlist.Listgame()
#remove.Removebyname(name="Benzema")
#remove.Removebyappid(appid="50")
