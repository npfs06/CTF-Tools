#coding:utf-8
import zipfile
import string
import binascii
s=["��ɫ", "��ɫ","��ɫ","��ɫ","��ɫ"]
def CrackCrc(crc):
    for i in dic:
        for j in dic:
            for p in dic:
                for q in dic:
                    s = i + j + p + q
                    if crc == (binascii.crc32(s) & 0xffffffff):
                        f.write(s)
                        return
 
def CrackZip():
    for I in s :
        file = I+'.zip'
        f = zipfile.ZipFile(file, 'r')
        GetCrc = f.getinfo('data.txt')
        crc = GetCrc.CRC
        CrackCrc(crc)
 
dic = string.ascii_letters + string.digits + '+/='
 
f = open('out.txt', 'w')
CrackZip()
f.close()