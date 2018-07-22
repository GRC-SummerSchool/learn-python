from math import sqrt

class Shape:

    def __init__(self,nSides,area):
        self.nSides=nSides
        self.area=area

    def grow(self,multiplier):
        self.area = self.area * multiplier

    def isbigger(self,otherShape):
        if not isinstance(otherShape,Shape):
            raise TypeError("Can only compare to other Shapes")

        # Returns True, False, or None if both are equal
        if self.area==otherShape.area:
            return None
        return self.area>otherShape.area


class Circle(Shape):

    PI = 3.14159

    def __init__(self,radius):
        super().__init__(360,0)
        self.radius = radius

    def _get_r(self):
        return self._r
    def _set_r(self,r):
        self._r = r
        self.area = self.PI * r**2

    radius = property(fget=_get_r,fset=_set_r)

    def grow(self,multiplier):
        self.radius = sqrt(multiplier) * self.radius

class Rectangle(Shape):

    def __init__(self,width,height):
        area=width*height
        super().__init__(4,area) # Shape.__init__(nSides) - Rectangle has 4 sides, always

        self._w = width # Otherwise get "height not yet set" issue when calculating area
        self.height = height

    def _set_w(self,w):
        self._w = w
        self.area = self.width*self.height
    def _get_w(self):
        return self._w
    width = property(fset = _set_w, fget = _get_w)

    def _set_h(self,h):
        self._h = h
        self.area = self.width*self.height
    def _get_h(self):
        return self._h
    height = property(fset = _set_h, fget = _get_h)

    def grow(self,multiplier):
        # Grow the rectangle's area while keeping the aspect ratio the same
        self._w = sqrt(multiplier) * self.width
        self.height = sqrt(multiplier) * self.height


class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)

    def _set_w(self,w):
        self._w = w
        self._h = w
        self.area = w**2

    _set_h = _set_w # Same function to set the width as the height

    # Redefine properties, since they work off function handles
    width=property(fset=_set_w,fget=Rectangle._get_w)
    height=property(fset=_set_h,fget=Rectangle._get_h)



if __name__=="__main__":
    rect = Rectangle(3,4)
    rect.grow(4)
    print(rect.width,rect.height,rect.area)

    square = Square(3)
    square.grow(4)
    print(square.width, square.height, square.area)

    circ = Circle(3.4)
    print(circ.isbigger(square), circ.area)
