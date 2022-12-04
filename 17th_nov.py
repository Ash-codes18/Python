class college:
    def  __init__(self,f1,f2):
        self.f1=f1
        self.f2=f2  
    def display(self):
        print(self.f1,self.f2)
class div(college):
    pass
x=div("Hakuna",5*25)
x.display()