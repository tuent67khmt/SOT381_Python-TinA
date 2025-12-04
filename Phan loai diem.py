diem_so=[8.5,7.0,9.2,6.8,5.5,8.8]
for i in diem_so:
    if i>=8:
        x='Gioi'
    elif 6.5<=i<=7.9:
        x='Kha'
    else:
        x='TB'
    print(i,"=>",x)
       