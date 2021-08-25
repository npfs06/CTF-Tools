//利用工具php_mt_seed之前，先用脚本将伪随机数转换成php_mt_seed可以识别的数据
<?php
$pass = "Ixy30EE6tN"; //密钥
$alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';//字母表
$len = strlen($alphabet) - 1; //区间长度
for($j = 0; $j < strlen($pass); $j++) //遍历密钥，确定当前字符在密钥的顺序
{
    for ($i = 0; $i <= $len; $i++) { //遍历字母表，确定当前字符在字母表的顺序
        if($pass[$j] == $alphabet[$i])//是找到了对应的随机数
        {
            echo "$i $i 0 $len "; //输出符合要求的参数格式
            break;
        }
    }
}
?>