"""nhập 3 số thực x,y,z
viết các chương trình tính toán số học
print ra màn hình x+y=z"""

x=int(input("nhập x="))
y=int(input("nhập y ="))
z=x+y
print("{0}+{1}={2}".format(x,y,z))#phép cộng
z=x-y
print("{0}-{1}={2}".format(x,y,z))#phép trừ
z=x*y
print("{0}*{1}={2}".format(x,y,z))#phép nhân
z=x/y
print("{0}/{1}={2}".format(x,y,z))#phép chia
z=x%y
print("{0}%{1}={2} đây là phép chia lấy phần dư".format(x,y,z))#phép chia lấy dư
z=x//y
print("{0}//{1}={2}".format(x,y,z))#pháp chia lấy phần nguyên2


"""bài 2
viết chương trình nhập 3 số thực a , b, c sau đó in kết quả màn hình phép so sánh của 3 số đó 
in ra màn hình kết quả dạng and , or, not 
"""
a=int(input('nhập a='))
b=int(input('nhập b='))
c=int(input('nhập c='))
z=a>0 and b<=20 and c!=25 
print('z',z)
z= a!=10 or b>100 and c ==78
print('z',z)
z=not(a>0 and b==87  or c>=15)
print("z",z)


""" bài 3
viết chương trình nhập số nguyên a và x 
in ra màn hình các phép toán tử gán của a và x """


a=int(input("nhập a"))
x=int(input("nhập x"))

a+=x
print("a+=x =>a=",a)
a-=x
print("a-=x =>a=",a)
a/=x
print("a/=x =>a=",a)
a*=x
print("a*=x =>a=",a)
a**=x
print("a^=x =>a=",a)
a%=x
print("a%=x =>a=",a)