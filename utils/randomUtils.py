#coding:utf-8

import random
import string
random_str=['1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def getRandomStr(n):
    str=''
    for i in range(n):
        j=random.randint(0,len(random_str))
        str+=random_str[j]
    return str

# if __name__=='__main__':
#     print(getRandomStr(64))