class Student:
    pass

alex = Student()
alex.name = "Alex"

kate = Student()
kate.name = "Kate"

nikita = Student()

alex = nikita
kate = alex

print(f"{alex.name}, {kate.name}, {nikita.name}")