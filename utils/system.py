#coding:utf-8

# 系统信息工具类
import psutil
import platform

def getSystemInfo():
    cpuCount=psutil.cpu_count()
    memory=psutil.virtual_memory().total;
    disk=getDiskTotal();
    osVersion=platform.system()
    ipAddress=getIPAddress()
    systemInfo=SystemInfo(osVersion,cpuCount,memory,disk,ipAddress)
    return systemInfo
def getIPAddress():
    ipDic=psutil.net_if_addrs()
    ipAddress=[]
    for k,v in ipDic.items():
        for item in v:
            if item[0]==2 and not item[1]=='127.0.0.1' and not item[1].startswith('169.254'):
                ipAddress.append(item[1])
    return ipAddress

def getDiskTotal():
    total=0
    partitions=psutil.disk_partitions()
    for item in partitions:
        if item.fstype!='':
            total+=psutil.disk_usage(item.device).total
    return total        

class SystemInfo:
    def __init__(self,os,cpu,memory,disk,ipAddress):
        self.os=os
        self.cpu=cpu
        self.memory=memory
        self.disk=disk
        self.ipAddress=ipAddress

# if __name__=='__main__':
#     print(getDiskTotal())