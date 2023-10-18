# Creating a Class
class Dog():
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(self.name + " is barking.")


my_dog = Dog('Tomi')
print(my_dog.name + " is a great dog!")
my_dog.bark()