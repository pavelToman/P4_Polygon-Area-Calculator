class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        a = self.width * self.height
        return a

    def get_perimeter(self):
        b = (2*self.width) + (2*self.height)
        return b

    def get_diagonal(self):
        c = ((self.width ** 2) + (self.height ** 2)) ** .5
        return c
    def get_picture(self):
        if self.height>50 or self.width>50:
            return "Too big for picture."
        else:
            pic = ""
            for i in range(self.height):
                for j in range(self.width):
                    pic += "*"
                if i < (self.height):
                    pic += "\n"
            return pic

    def get_amount_inside(self, obj):
        a = obj.height * obj.width
        b = self.get_area()
        c = b // a
        return c

class Square(Rectangle):
    def __init__(self, a):
        self.height = a
        self.width = a
    def __repr__(self):
        return f"Square(side={self.height})"
    
    def set_side(self,a):
        self.height = a
        self.width = a
    
    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.height = height
        self.width = height

r1 = Rectangle(3,5)
print(r1)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.get_diagonal())
r1.set_height(6)
print(r1)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.get_diagonal())
print(r1.get_picture())
r2 = Rectangle(1,3)
print(r1.get_amount_inside(r2))

s1 = Square(4)
print(s1)
print(s1.get_area())
print(s1.get_perimeter())
print(s1.get_diagonal())
print(s1.get_picture())
print(s1.get_amount_inside(r2))
s1.set_height(8)
print(s1)
s1.set_width(9)
print(s1)