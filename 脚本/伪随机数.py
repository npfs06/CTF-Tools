//���ù���php_mt_seed֮ǰ�����ýű���α�����ת����php_mt_seed����ʶ�������
<?php
$pass = "Ixy30EE6tN"; //��Կ
$alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';//��ĸ��
$len = strlen($alphabet) - 1; //���䳤��
for($j = 0; $j < strlen($pass); $j++) //������Կ��ȷ����ǰ�ַ�����Կ��˳��
{
    for ($i = 0; $i <= $len; $i++) { //������ĸ��ȷ����ǰ�ַ�����ĸ���˳��
        if($pass[$j] == $alphabet[$i])//���ҵ��˶�Ӧ�������
        {
            echo "$i $i 0 $len "; //�������Ҫ��Ĳ�����ʽ
            break;
        }
    }
}
?>