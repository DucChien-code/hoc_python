import math


def kiem_tra(a, b, c):
    if a == 0:
        nghiem = -b/a
    else:
        landa = b*b - 4*a*c
        if landa < 0:
            print("Phương trình vô nghiệm ❤️")
        elif landa == 0:
            nghiem = -b/2*c
        else:
            nghiem1 = (-b - math.sqrt(landa))/2*a
            nghiem2 = (-b + math.sqrt(landa))/2*a
    return nghiem


a = int(input("Nhap a= "))
b = int(input("Nhap b= "))
c = int(input("Nhap c= "))
print(kiem_tra(a, b, c))
