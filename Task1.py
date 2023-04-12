class Person:

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def hello(self):
        print(f'Hello, my name is {self.firstname} {self.lastname}. I am {self.age}')


class Student(Person):

    def __init__(self, firstname, lastname, age, grade):
        super().__init__(firstname, lastname, age)
        self.grade = grade

    def studhello(self):
        print(f'Hello, my name is {self.firstname} {self.lastname}. I am a {self.grade} grade student')


class Teacher(Person):

    def __init__(self, firstname, lastname, age, salary):
        super().__init__(firstname, lastname, age)
        self.salary = salary

    def teachhello(self):
        print(f'Hello, my name is {self.firstname} {self.lastname}. I am paid {self.salary} a month')

pers = Person('Man', 'Human', 55)
pers.hello()

stud = Student('Guy', 'Boy', 12, 6)
stud.hello()
stud.studhello()

prof = Teacher('Dude', 'Person', 40, 200)
prof.hello()
prof.teachhello()