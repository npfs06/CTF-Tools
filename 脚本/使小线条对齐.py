from PIL import Image

img = Image.open("img.png")

l = []
c = []

for x in range(img.size[0]):
    l.append([])
    c.append([])
    for y in range(img.size[1]):
        pixel = img.getpixel((x, y))
        if pixel == (255, 0, 0):
            c[x].append(y)
        l[x].append(pixel)

m = min([i[0] for i in c])

new_img = Image.new("RGB", (img.size[0], img.size[1]), (255,255,255))

for x in range(img.size[0]):
    p = c[x][0] - m
    for y in range(img.size[1]):
        pixel = img.getpixel((x, y))
        py = (img.size[1] + y - p) % img.size[1]
        new_img.putpixel((x, py), pixel)
new_img.save("new.png")