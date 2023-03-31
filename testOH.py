import tkinter as tk
# tạo hộp thoại Hiển thị thông tin, tkk tạo giao diện đẹp
from tkinter import messagebox, ttk

USER_NAME = "chien071202"
PASSWORD = "1234"

# Định nghĩa function tạo ra chức năng kiểm tra đăng nhập có thành công không.


def click():
    user_name = txt_user_name.get()
    password = txt_password.get()

    if user_name == USER_NAME and password == PASSWORD:
        messagebox.showinfo("Info", "Login thành công")
    else:
        messagebox.showerror("Error", "Login thất bại")


# Tạo giao diện
root = tk.Tk()  # tạo ra một cửa sổ chính
root.title("Duc Chien")  # Thay đổi tiêu đề cửa sổ
root.geometry("400x200+800+200")  # Thay đổi chiều rộng, chiều cao
# root.iconbitmap("smile2.ico")  # thêm icon
root.resizable(False, False)  # Không cho phép thay đổi chiều rộng và chiều cao
root.config(bg="#2a9d8f")  # Thay đổi màu nền

# grid layout manger: Quản lí bố cục lưới dạng ngang
lbt_text = tk.Label(root, text="USER_NAME", bg="orange",
                    fg="black")  # Tạo ra một label có màu và chữ
lbt_text.grid(row=0, column=0, padx=(30, 0), pady=(20, 0))
# lbt_text.pack()  # đặt label lên cửa sổ

txt_user_name = tk.Entry(root, width="30")  # tạo ra một cửa sổ để nhập dữ liệu
txt_user_name.grid(row=0, column=1, padx=(30, 0), pady=(20, 0))
# txt_user_name.pack()  # đặt vào

# bg: Màu nền, fg: Màu chữ

lbl_pass = tk.Label(root, text="Password", bg="#fefae0",fg="black")  # Tạo ô nhập mật khẩu
lbl_pass.grid(row=1, column=0, padx=(30, 0))
# lbl_pass.pack(pady=(20, 0))  # pady: Kích thước theo chiều rộng

# Nhập dữ liệu Password, show: Hiện thị mật khẩu nhập bằng kí tự *
txt_password = tk.Entry(root, width="30", show="*")
txt_password.grid(row=1, column=1, padx=(30, 0), pady=20)

# Tạo ra nút bấm kiểm tra đăng nhập
# tạo nút bấm kiểm tra,

# tkk tạo giao diện đẹp hơn nút submit
btn_submit = ttk.Button(root, text="Submit", command=click)
# btn_submit.pack(pady=(20, 0))
btn_submit.grid(row=2, column=1, ipadx=5, ipady=5)

root.mainloop()  # Hiện thị cửa sổ đến khi tắt
