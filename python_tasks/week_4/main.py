class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old. I am a {self.gender}")
        
person1 = Person("Scott", 21, "Male")
person1.introduce()
