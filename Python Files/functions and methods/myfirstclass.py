class Dog():

    def __init__(self,breed,name):
        self.breed=breed
        self.name=name
        print(f"my name is {self.name} and breed is {self.breed} and I say WOOF WOOF")


my_dog=Dog("Sammy","Lab")
my_dog.breed