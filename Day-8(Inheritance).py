class College:
    def __init__(self,n,loc):
        self.name=n
        self.location=loc
    def info(self):
        print(self.name + " is located in " + self.location)

class Department(College):
    def __init__(self,ids,n):
        self.id=ids
        self.name=n
        super().__init__(n," GEC Vaishali ")
    def info_d(self):
        print(self.id + " is department code of " +self.name)

D=Department("155", "CSE(IOT)")
D.info_d()
D.info()
