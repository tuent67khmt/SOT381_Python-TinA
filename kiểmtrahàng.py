sl=[15,8,22,5,12,3]
sp=['Áo','Quần','Giày','Túi','Mũ','Ví']
for a in range(len(sl)):
    if sl[a]<10:
        print(f"Cần nhập thêm : {sp[a]}")
    else:
        print(f"Đủ hàng: {sp[a]} ({sl[a]})")
