import requests
import re
# ������վ�Ự
s = requests.session()
# ����get����
u = s.get("http://123.206.87.240:8002/qiumingshan/")
# ��ȡ��վ�ļ���ʽ��a��u.text����������վ���ص�ҳ������
a = re.search(r'(\d+[+\-/*])+(\d+)', u.text)
# ����һ���ֵ�zd����"value"����ֵΪ�ղ�ƥ���ʽ�ӵ�ֵ
# eval����ʽ�ӵ�ֵ
zd = {
        "value": eval(a.group(0))
}
# ����post����
u = s.post("http://123.206.87.240:8002/qiumingshan/", data=zd)
print(u.text)