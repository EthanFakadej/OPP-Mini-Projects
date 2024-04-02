class Professor:
    
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        
    def greet_students(self):
        print("Welcome to class!")

# Write your code below:
        
class ISMProfessor(Professor):
    def __init__(self, name, age, course):
        super().__init__(name, age, course)

    def greet_students(self):
        print("Hi everyone! It's a greta day to study ISM 480!")
        super().greet_students()

my_ism_professor = ISMProfessor("bo",34,"ism 480")
my_ism_professor.greet_students()