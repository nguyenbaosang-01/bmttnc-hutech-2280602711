# nhap cac dong tu nguoi dung 
print("nhap cac dong van ban (Nhap'done' de ket thuc):")
lines = []
while True:
    line=input()
    if line.lower() =='done':
        break
    lines.append(line)
    #chuyen cac dong thanh chu in hoa va in ra man hinh
    print("/nCac dong da nhap sau khi chuyen chu in hoa :")
    for line in lines:
        print(line.upper())
        
    



