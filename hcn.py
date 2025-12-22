def hcn(w,h):
    return w,h

while True:
    w=float(input('Nhập chiều dài '))
    h=float(input('Nhập chiều rộng '))
    if 0.0<=w and h<=100:
        cv=(w+h)*2
        dt=(w*h)
        print(f"chu vi hcn: {cv:9.1f}")
        print(f"dien tich hcn: {dt:9.1f}")
    else:
        print('vui long nhap lai\n')

