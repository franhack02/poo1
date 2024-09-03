#crear un metodo que devuelva el punto al origen

class Point:
    def move (self,x,y):
        self.x = x
        self.y = y
    
    def origin(self): #metodo para devoler el punto al origen
        self.y = 0
        self.x = 0

p1 = Point()
p2 = Point()

print(p1,p2)

p1.move(5,5)
p2.move(5,9)
print(p1.x,p1.y)
print(p2.x,p2.y)

p1.origin()
p2.origin()
print(p1.x,p1.y)
print(p2.x,p2.y)



