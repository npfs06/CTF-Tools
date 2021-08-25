import string

if __name__ == "__main__":
    s = string.printable[62:62+32] ##代表    !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    s1 = string.printable[:62]     ##代表    0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    for i in s:
        for j in s:
            x = chr(ord(i)^ord(j))
            if x in s1+'_':
                print '{0}\t{1}\t{2}'.format(i,j,x)
                
 //结果如下
!	@	a
!	[	z
!	`	A
!	{	Z
!	~	_
"	@	b
"	[	y