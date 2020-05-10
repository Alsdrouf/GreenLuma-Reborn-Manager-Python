#Importing
import sys
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
print(workpath)

sys.path.append(str(workpath))
add.Test()
add.Adding(workpath, 50)
