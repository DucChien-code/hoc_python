class Student:
    def __init__(self, name, age, address, classe):
        self.name = name
        self.age = age
        self.address = address
        self.classe = classe
    
    def show_info(self):
        print(f''' STUDENT INFO👌
Name: {self.name}❤️
Age: {self.age}❤️
Address: {self.address}❤️
Class: {self.classe}❤️''')
    def __str__(self) -> str:
        return f"<Student(name={self.name},age={self.age})>"
    def __gt__(self, other):
        return self.age > other.age

Ten = input("Nhap ten: ")
Tuoi = input("Nhap tuoi: ")
Que = input("Nhap que quan: ")
Lop_hoc = input("Lop cua ban: ")

out_student = Student(Ten, Tuoi, Que, Lop_hoc)

out_student.show_info()
