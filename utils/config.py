#coding:utf-8
import os
import configparser
configName='config.conf'

def init():
    print('init config')
    confEdit=os.path.isfile(configName)
    if not confEdit:
        print('creat config')
        open(configName,'w')
    global conf
    conf=configparser.ConfigParser()
    conf.read(configName,'utf-8')

def write():
    configFile=open(configName,'w')
    conf.write(configFile)

if __name__=='__main__':
    init()