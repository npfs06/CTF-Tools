import zlib
import struct

filename = 'mod.png'
with open(filename, 'rb') as f:
    all_b = f.read()
    crc32key = int(all_b[29:33].hex(),16)
    data = bytearray(all_b[12:29])
    n = 4095            #������0xffffffff,�����ǵ���Ļʵ��/cpu��0x0fff�Ͳ����
    for w in range(n):          #�ߺͿ�һ����
        width = bytearray(struct.pack('>i', w))     #qΪ8�ֽڣ�iΪ4�ֽڣ�hΪ2�ֽ�
        for h in range(n):
            height = bytearray(struct.pack('>i', h))
            for x in range(4):
                data[x+4] = width[x]
                data[x+8] = height[x]
            crc32result = zlib.crc32(data)
            if crc32result == crc32key:
                print("��Ϊ��",end="")
                print(width)
                print("��Ϊ��",end="")
                print(height)
                exit(0)