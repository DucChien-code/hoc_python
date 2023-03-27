import random
import string

def generate_password(length):
    """
    Chức năng này tạo ra một mật khẩu ngẫu nhiên có độ dài nhất định bằng cách sử dụng kết hợp chữ hoa, chữ thường, chữ số và ký tự đặc biệt
    """
    # Xác định một chuỗi chứa tất cả các ký tự có thể
    all_chars = string.ascii_letters + string.digits + string.punctuation
    # Tạo mật khẩu bằng cách sử dụng lựa chọn ký tự ngẫu nhiên
    pass_word = "".join(random.choice(all_chars) for i in range(length))

    return pass_word

password = int(input("Mời bạn nhập độ dài mật khẩu: "))

pass_ = generate_password(password)
print(pass_)

