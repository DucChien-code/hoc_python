try:
    f = open("demofile.txt")
    try:
        f.write("Duc Chien")
    except:
        print("Đã xảy ra lỗi khi ghi vào tệp!")
    finally:
        print("Bạn đã cố gắng rồi!")
except:
    print("Đã xảy ra lỗi khi mở tệp!")


# Tăng TypeError nếu x không phải là số nguyên:
x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")
