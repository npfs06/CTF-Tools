from PIL import Image

x = 141    #x����  ͨ����txt�����������������
y = 726    #y����  x * y = ����
im = Image.new("RGB", (x, y))
file = open('1.txt')

for i in range(0, x):
    for j in range(0, y):
        line = file.readline()  #��ȡһ�е�rgbֵ
        line = line[:-2]
        line = line[1:]
        #print(line)
        rgb = line.split(", ")  #����rgb���ı��ж��ź����пո�
        im.putpixel((i, j), (int(rgb[0]), int(rgb[1]), int(rgb[2])))
im.save('test2.png')