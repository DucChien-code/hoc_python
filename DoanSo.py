import random

secret_number = random.randint(1,100)
solandoan = 1
while True:
    iswin = False
    guess = int(input("Mời bạn nhập số đoán trong khoảng từ 1 đến 100: "))
    print(f"Bạn đoán lần thứ: {solandoan}")

    if guess > secret_number:
        print(f"Số bạn nhập lớn hơn số máy!" )
        solandoan +=1       
    elif guess < secret_number:
        print(f"Số bạn nhập nhỏ hơn số máy!")
        solandoan +=1
    else:
        print(f"Congratutions! Bạn đã đoán đúng❤️, số máy là: {secret_number}")
        iswin = True
        break
    if solandoan ==7:
        print(f"Bạn đã hết lượt chơi!")
        break

while True:
    if iswin != True:
        print(f"GAME OVER!, Số máy là: {secret_number}")
    d = input("Bạn có muốn tiếp tục không? (c/k)")
    if d == "k":
        break
    continue

print("GOOD BYE❤️")