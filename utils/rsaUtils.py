#coding:utf-8
#非对称密钥RSA工具类
import rsa
from binascii import b2a_hex,a2b_hex 

#生成ras密钥对并保存在本地
#public.pem+private.pem
def generateKeys():
    (pubKey,priKey)=rsa.newkeys(1024)
    with open('public.pem','w+') as f:
        f.write(pubKey.save_pkcs1().decode())
    with open('private.pem','w+') as f:
        f.write(priKey.save_pkcs1().decode())

#加密信息
#keyPath 公钥地址
#msg 加密信息
def encrypt(keyPath,msg):
    with open(keyPath,'r') as f:
        pubKey=rsa.PublicKey.load_pkcs1(f.read().encode())
        crypto=rsa.encrypt(msg.encode(),pubKey)
        return str(b2a_hex(crypto))
    return ''

#解密信息
#keyPath 私钥地址
#msg 进行揭秘的字符串
def decrypt(keyPath,msg):
     with open(keyPath,'r') as f:
        priKey=rsa.PrivateKey.load_pkcs1(f.read().encode())
        result=rsa.decrypt(a2b_hex(msg),priKey).decode()
        return result
     return ''
if __name__=='__main__':
    aa=encrypt('public.pem','hello world')

    print(decrypt('private.pem',aa))