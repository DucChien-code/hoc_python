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

class People:
    def __init__(self, birthday) -> None:
        self.birthday = birthday
    @property # coi các hàm như là một thuộc tính
    def get_age(self):
        return 2023 - self.birthday

people1 = People(2003)

age = people1.get_age

print(age)

class Human:
    def __init__(self, name):  
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}"


class Student(Human):
    def __init__(self, name, age):
        super().__init__(name) # super() gọi class Human tạo object
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, age: {self.age}"


student_one = Student("Chien", 20)
print(student_one)
