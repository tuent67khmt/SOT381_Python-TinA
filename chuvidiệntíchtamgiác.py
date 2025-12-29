def dt_tamgiac(a,b,c):
    return a,b,c

while True:
    a=int(input('Nhập cạnh 1 '))
    b=int(input('Nhập cạnh 2 '))
    c=int(input('Nhập cạnh 3 '))
    if a+b>c and a+c>b and b+c>a:
        cv=a+b+c
        p=cv/2
        dt=(p*(p-a)*(p-b)*(p-c))**0.5
        print('Chu vi tam giác',cv)
        print('Diện tích tam giác',dt)
        break
    else:
        print('3 cạnh tam giác không hợp lệ!\n')
        
