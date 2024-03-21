class Person:
    def __init__(self,name,age,gender):
        self.name= name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f'hello my name is {self.name}, I am {self.age} years old and I am {self.gender}')
       
 #create an instance of class
person = Person(name='Carolyne',age= 20, gender='feamle')
person.introduce()