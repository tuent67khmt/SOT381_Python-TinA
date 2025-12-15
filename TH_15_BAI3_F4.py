s=0
s2=10
n=int(input('nhap n '))
for i in range (1,n+1):
    s+=1/i
print("s",s)
for j in range (1,n+1):
    s2+=((j-1)/j)

print('s2',s2)