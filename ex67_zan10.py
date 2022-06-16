# 1. дефиниция на класа
#  
from math import sqrt


class Point:
    # данни на класа (статични)
    count = 0

    def __init__(self, *, x=0, y=0):
        print('--- init obj ---')
        # данни на обекта
        self.x = x
        self.y = y
        Point.count += 1

    # методи на обекта
    def draw(self):
        print(f'draw point at ({self.x}, {self.y} ) count:{Point.count}')


    def move_to(self, dx, dy):
        self.x += dx
        self.y += dy

    # методи за достъп до данните
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        assert x >= 0, f'negative values for x not supported ({x})'
        self.__x = x

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        assert y >= 0, f'negative values for y not supported ({y})'
        self.__y = y
    # специални методи

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self,other):
        if not isinstance(other, Point):
            raise NotImplementedError('Not yet implemented')
        return self.x == other.x and self.y == other.y

    def __gt__(self,other):
        if not isinstance(other, Point):
            raise NotImplementedError('Not yet implemented')
        
        dx1 = self.x ** 2
        dy1 = self.y ** 2
        dist1 = sqrt(dx1 + dy1)

        dx2 = other.x ** 2
        dy2 = other.y ** 2
        dist2 = sqrt(dx2 + dy2)

        return dist1 > dist2

    def __add__(self, other):
        new_x, new_y = 0,0

        if isinstance(other, Point):
            new_x = self.x + other.x
            new_y = self.y + other.y
        elif isinstance(other, (int,float)):
            new_x = self.x + other
            new_y = self.y + other
        else:
            raise NotImplementedError('Not yet implemented')

        # return self
        return Point(x = new_x, y = new_y)

    def __del__(self):
        Point.count -= 1
        print(f'Object ({self.x}, {self.y}) count:{Point.count}')

if __name__ == '__main__':
    # 2. създаване на обект от дадения тип
    # клас -> Point, обект -> екземпляр, представител на класа p1
    print(f'Point.count:{Point.count}')

    p1 = Point(x = 10, y = 20)
    p1.draw()

    p2 = Point(x = 2, y = 5)
    p2.draw()

    del p1
    p2.draw()

    
    print('---')