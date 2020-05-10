#Importing
import sys
import os
import configparser as config
sys.path.append('./Function')
import AddingFile as add
import Reorder as reorder
import Option as option
import Getlist as getlist
sys.path.append('../')

config = config.ConfigParser()
config.read('settings.ini')
workpath = config['GENERAL']['Workpath']
os.chdir(workpath)
workpath = os.getcwd()
print(workpath)

#for loop in range(10):
#    numberoffile=len(getlist.Listfile(workpath=workpath))
#    print(getlist.Listfile(workpath=workpath))
#    add.Adding(workpath=workpath, number=numberoffile, appid=50)
reorder.Reorder()
