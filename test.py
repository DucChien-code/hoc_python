# lấy thông tin sách người dùng nhập
def add_book():
    title = input("Tên sách: ").strip().title()
    author = input("Tác giả: ").strip().title()
    year = input("Năm phát hành: ").strip().title()

    with open("data.csv", "a") as reading_list:
        reading_list.write(f"{title}, {author},{year}\n")

# Tìm kiếm một cuốn sách
def find_books():
    reading_list = get_all_books()
    matching_books = []

    search_term = input("Vui lòng nhập tên sách để tìm kiếm: ").strip().lower()

    for book in reading_list:
        if search_term in book["title"].lower():
            matching_books.append(book)


    return matching_books

# Lấy dữ liệu sách ra khỏi tệp

def get_all_books():
    books = []

    with open("data.csv", "r") as reading_list:
        for book in reading_list:
            # Trích xuất các giá trị từ file CSV
            title, author, year = book.strip().split(",")

            # Tạo một từ điển từ dữ liệu csv và thêm nó vào danh sách sách

            books.append({
                "title": title,
                "author": author,
                "year": year
            })
            
    return books

# Hiển danh danh sách sách đã nhập
def show_books(books):
    # Thêm một dòng trống trước đầu ra
    print()

    for book in books:
        print(f"{book['title']}, by {book['author']} ({book['year']})")

    print()


menu_prompt = """Vui lòng chọn một trong các tùy chọn sau:
- 'a' thêm một cuốn sách
- 'l' liệt kê những cuốn sách
- 's' tìm kiếm một cuốn sách
- 'q' thoát


Lựa chọn của bạn là?"""
# Nhận sự lựa chọn của người dùng
selected_option = input(menu_prompt).strip().lower()

# Chạy lòng lặp cho đến khi người dùng chọn 'q'
while selected_option != "q":
    if selected_option == "a":
        add_book()
    elif selected_option == "l":
        # Truy xuất toàn bộ danh sách đọc để in
        reading_list = get_all_books()


        # Kiểm tra xem reading_list có chứa ít nhất một cuốn sách không
        if reading_list:
            show_books(reading_list)
        else:
            print("Danh sách đọc của bạn trống")

    elif selected_option == "s":
        matching_books = find_books()

        # Kiểm tra xem tìm kiếm đã trả lại ít nhất một cuốn sách
        if matching_books:
            show_books(matching_books)
        else:
            print("Rất tiếc, chúng tôi không tìm thấy bất kỳ cuốn sách nào cho cụm từ tìm kiếm đó.")
    else:
        print(f"Xin lỗi, '{selected_option}' không phải là một lựa chọn hợp lệ. ")

    # Cho phép người thay đổi lựa chọn ở cuối mỗi lần lặp
    selected_option = input(menu_prompt).strip().lower()
