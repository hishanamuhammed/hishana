class Rect:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return(self.length*self.breadth)
    def pere(self):
        return(2*(self.length+self.breadth))
r1=Rect(4,5)
r2=Rect(9,3)
print(r1.area())
print(r1.pere())
print(r2.area())
print(r2.pere())
a1=r1.area()
a2=r2.area()
if(a1>a2):
    print("first rectangle is bigger than second")
else:
    print("second rectangle is bigger than first")



