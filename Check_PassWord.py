"""
Xây dựng một trình kiểm tra mật khẩu. Công việc của nó là kiểm tra xem mật khẩu có đủ mạnh hay không dựa trên một số tiêu chí đặt ra. Nó sẽ in lỗi nếu bất kỳ tiêu chí mật khẩu nào không được đáp ứng.
"""
def password_checker(password):
    # Xác định tiêu chí cho mật khẩu mạnh
    min_length = 8
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special_char = False
    special_chars = "!@#$%^&*()-_=+[{]}\|;:',<.>/?"

    # Kiểm tra độ dài mật khẩu
    if len(password) < min_length:
        print("Mật khẩu quá ngắn!")
        return False
    
    # Kiểm tra xem mật khẩu có chứa chữ hoa, chữ thường, chữ số và ký tự đặc biệt không
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special_char = True

    # In thông báo lỗi cho từng tiêu chí bị lỗi
    if not has_uppercase:
        print("Mật khẩu phải chứa ít nhất một chữ cái viết hoa!")
        return False
    if not has_lowercase:
        print("Mật khẩu phải chứa ít nhất một chữ cái viết thường!")
        return False
    if not has_digit:
        print("Mật khẩu phải chứa ít nhất một chữ số!")
        return False
    if not special_chars:
        print("Mật khẩu phải chứa ít nhất một kí tự đặc biệt!")
        return False
    # Nếu tất cả các tiêu chí được đáp ứng, in một thông báo thành công
    print("Mật khẩu mạnh!")
    return True

# Nhắc người dùng nhập mật khẩu và kiểm tra xem nó có đáp ứng tiêu chí không
password = input("Mời bạn nhập mật khẩu mạnh: ")
password_checker(password)
