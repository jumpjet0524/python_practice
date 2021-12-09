# #Point 實體物件的設計:平面座標上的點

# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def show(self):
#         print(self.x,self.y)
#     def distance(self,targetx,targety):
#         print(((self.x-targetx)**2+(self.y-targety)**2)**0.5)
        
# p=Point(5,12)
# p.show()
# p.distance(0, 0)

class File:
    def __init__(self,name):
        self.name=name
        self.file=None
    def open(self):
        self.file=open(self.name,mode="r",encoding="utf-8")#內建
    def read(self):
        return self.file.read()
    
f=File("data.txt")
f.open()
data=f.read()
print(data)
        
        