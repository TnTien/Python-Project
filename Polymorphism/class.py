
#Parent Class
class Person:
    # Used to create a new object
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    # Method that will print out message, will also be inherited by child classes
    def info(self):
        msg = "\n{} is {} years old. Email: {}".format(self.name, self.age, self.email)
        return msg

#Child Classes
class Student(Person):
    #Attributes
    current_student = True
    # Used to create a new object for Student class
    def __init__(self, name, age, email, year_enrolled):
        # super() function that will make the child class inherit all the methods and properties from it's parent class
        super().__init__(name, age, email)
        # Used to add a new property to Student Class
        self.year_enrolled = year_enrolled
    # Method for Student class
    def student(self):
        msg = "\n{} is also a student. Enrollment year: {}".format(self.name, self.year_enrolled)
        return msg

class Staff(Person):
    employee = True
    def __init__(self, name, age, email, years_worked):
        super().__init__(name, age, email)
        self.years_worked = years_worked

    def staff(self):
        msg = "\n{} is currently working here. Years worked: {}".format(self.name, self.years_worked)
        return msg
#Creates instance of Person class
p1 = Person("John", 36, 'tim@gmail.com')
#Creates instance of Student class
student1 = Student("Tim", 20, "123@yahoo.com", 2019)
#Creates instance of Staff class
staff1 = Staff("Joe", 25, "joe123@hotmail.com", 5)

print(p1.info())
print(student1.info() + student1.student())
print(student1.current_student)
print(staff1.info() + staff1.staff())
print(staff1.employee)



