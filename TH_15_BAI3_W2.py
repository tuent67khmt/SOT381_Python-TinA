    
gt=1
while True:    
    n=int(input('Nhap n'))
    if 0 < n and n < 10 :
        for i in range(1,n+1,1):
            gt = gt * i
        break
print(gt)
        