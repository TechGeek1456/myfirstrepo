class circle():
    pi=3.14
    def __init__(self,radius):
        self.radius=radius

    def get_area(self):
        return self.pi*self.radius*self.radius

    def get_circumference(self):
        return 2*self.pi*self.radius   
        
my_circle=circle(10)
print(my_circle.get_area())
print(my_circle.get_circumference())