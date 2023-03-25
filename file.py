# File
"""
b1: open
b2: process
b3: close
"""
# fp = open("test.txt", mode='a')  # r => reading đọc file, a => append, w => writing

# data = fp.write("Le Duc Tiep\n")

# fp.close()

lst = ['a', 1, True, "c", 4.5]

fp1 = open("test.txt", mode="w")

data = fp1.write(' - '.join(map(str,lst)))

fp1.close()