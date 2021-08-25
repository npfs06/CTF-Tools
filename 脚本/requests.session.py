import requests
import re
# 保持网站会话
s = requests.session()
# 发送get请求
u = s.get("http://123.206.87.240:8002/qiumingshan/")
# 获取网站的计算式给a，u.text接收请求网站返回的页面内容
a = re.search(r'(\d+[+\-/*])+(\d+)', u.text)
# 创建一个字典zd，键"value"，键值为刚才匹配的式子的值
# eval计算式子的值
zd = {
        "value": eval(a.group(0))
}
# 发送post请求
u = s.post("http://123.206.87.240:8002/qiumingshan/", data=zd)
print(u.text)