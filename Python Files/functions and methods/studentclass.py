class student():
    college="xyz"    
        
    def __init__(self,id,name,branch,gender):
        self.id=id
        self.name=name
        self.branch=branch
        self.gender=gender
        print(f"{self.name} is {self.gender} studying in {self.branch} with rollno {self.id}")


s1=student(123,"raj",'cse','M')
