def stn(n):
    return n
n=int(input('Nhap n'))
if n%3==0:
    if n%2==0:
        print('số n là số chẵn chia hết cho 3')
    else: print("n là số chẵn không chia hết cho 3")
elif n%3==0 and n%2!=0:
    print('n khong phai la so chan va chia het cho 3')
else: print('n la so le k chia het cho 3')
