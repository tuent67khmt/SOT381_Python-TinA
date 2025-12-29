def bt(a):
    return a
a=int(input('Nhập số giây: '))
h=a//3600
p=(a%3600)//60
s=a%60
print(f"{h:02d}h:{p:02d}p:{s:02d}s")
