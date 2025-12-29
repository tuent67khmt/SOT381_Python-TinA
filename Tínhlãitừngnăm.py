von=100000000
lai_suat = 0.07
nam=20
print(f"Đầu tư vốn {von:,} VND với lãi suất {lai_suat*100}/năm")
for i in range(1, nam+1):
    von = von * (1+lai_suat)
    print(f"Năm{1}:{von:,.0f}VND")
    
print(f"Sau {nam} năm: {von:,.0f} VND")
