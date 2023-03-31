"""
Cách xây dựng một Web Scraper bằng Python
Trình quét web quét/lấy dữ liệu từ các trang web và lưu dữ liệu đó ở bất kỳ định dạng nào chúng tôi muốn, .csv hoặc .txt. Chúng ta sẽ xây dựng một công cụ quét web đơn giản trong phần này bằng cách sử dụng thư viện Python có tên là Beautiful Soup.
"""
import requests
from bs4 import BeautifulSoup

# Đặt URL của trang web bạn muốn Scrape
url = 'https://www.example.com'

# Gửi yêu cầu HTTP tới URL và truy xuất nội dung HTML
response = requests.get(url)

# Tạo một đối tượng BeautifulSoup phân tích nội dung HTML
soup = BeautifulSoup(response.content, 'html.parser')
# Tìm tất cả các liên kết trên trang web
links = soup.find_all('a')

# In văn bản và thuộc tính href của mỗi liên kết
for link in links:
    print(link.get('href'), link.text)