# 1. дефиниция на класа
#  
class Point:
    
    def __init__(self, *, x=0, y=0):
        print('--- init obj ---')
        # данни на обекта
        self.x = x
        self.y = y

    # методи на обекта
    def draw(self):
        print(f'draw point at ({self.x}, {self.y} )')


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
    

if __name__ == '__main__':
    # 2. създаване на обект от дадения тип
    # клас -> Point, обект -> екземпляр, представител на класа p1
    p1 = Point() 
    p2 = Point(x = 30, y = 40)

    p2.x = 200
    p2.y = 100

    p2.draw()

    # p2.x = -1
    print('---')