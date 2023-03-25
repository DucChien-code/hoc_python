# Mở file CSV
with open("2.csv", mode ='r', encoding="utf8") as file: #lấy cả giá trị có dấu
    for line in file:
        print(line.strip())

# Mở file json
import csv
import json

with open("medicine_dataset1.csv", mode = "r", encoding="utf8") as file:
    csv_file = csv.DictReader(file)
    lst = list(csv_file) # list[dict]
    print(json.dumps(lst, indent=4))

# json là một định dạng trao đổi dữ liệu nhẹ
# json được sử dụng để gửi dữ liệu giữa các máy tính khác nhau
# dump - ghi dữ liệu vào file json
# dumps - chuyển đổi một list[dict] hay dict thanh một chuỗi
# load - đọc dữ liệu từ file json => list[dict] hay dict
# loads - Chuyển đổi một string có dạng dict hay list[dict] thanh list[dict] hay dict tuong ung 

import json

with open("test.json", mode = "r") as file:
    lst = json.load(file) #đọc dữ liệu từ file json, dums trả về list dict
    print(json.dumps(lst, indent=4))

# Ghi vào file json
import json

student = [
    {
        'name': 'Bob',
        'age': 23
    },
    {
        'name': 'Chien',
        'age': 20
    }
]

with open("data1.json", mode = 'w') as file:
    json.dump(student, file, indent=4)