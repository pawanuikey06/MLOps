

class Employee :
    # Special /magic/dunder/constructor
    def __init__(self):
        print("Started Excecuting")
        self.Name ="Pawan"
        self.Id=123
        self.salary=50000
        print("Data Has Been Initialized")
    
    def Travel(self,destination):
        print(f"Employee is travling to {destination}")

    




sam =Employee()

sam.Travel("Nepal")

sam2=Employee()

print(sam.salary)

print(type(sam))



