# Parent Class
class User:
    # Attributes, will be inherited by child classes
    name = ""
    email = ""
    password = ""
    id_number = 0

# Child Classes
class Staff(User):
    job_title: ""
    base_pay: 0

class Student(User):
    active_student: True
    major: ""
    
    
    
