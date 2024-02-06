class Dog:
    def __init__(self, age, name, is_male, weight)
        self.age =age
        self.name = name
        self.is_male = is_male #Boolean, True if Male, False if female
        self.weight = weight

#Create an instance of this class
my_dog = Dog(1, "Moe", False, 5)

print(f'My dog is  {my_dog.age} year-old, her name is {my_dog.name}, her weight is {my_dog.weight}')

your_dog = Dog(2, "Victor", True, 10)

print(f'My dog is  {your_dog.age} year-old, her name is {your_dog.name}, her weight is {your_dog.weight}')

