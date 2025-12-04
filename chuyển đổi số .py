def chuyendoi(n):
    return n
n = int(input("Nhập một số thập phân: "))

if n >= 0:
    binary = bin(n)[2:]
else:
    binary = "-" + bin(n)[3:]   

print("Số nhị phân là:", binary)