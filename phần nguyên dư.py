def ND(m,n):
    return m,n
while True:
    m=int(input('Nhập số m '))
    n=int(input('Nhập số n '))
    if m>0 and n>0:
        print(' phần dư',m%n)
        print('phần nguyên',m//n)
        break
    else:
        print('Vui lòng nhập lại hai số nguyên')