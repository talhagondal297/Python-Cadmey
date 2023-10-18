# Inheritence
class Animal():
    def __init__(self, name):
        self.name = name
    def sit(self):
        print(self.name + " is sitting.")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def search(self):
        print(self.name + " is searching.")


my_dog = Dog('Sam')
print(my_dog.name + " is a search dog.")
my_dog.sit()
my_dog.search()