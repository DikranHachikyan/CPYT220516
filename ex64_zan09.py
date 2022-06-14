# 1. дефиниция на класа
#  
class Point:
    
    def __init__(self, *, x=0, y=0):
        print('--- init obj ---')
        # данни на обекта
        self.set_x(x)
        self.__y = y

    # методи на обекта
    def draw(self):
        print(f'draw point at ({self.get_x()}, {self.__y} )')


    def move_to(self, dx, dy):
        self.set_x( self.get_x() + dx)
        self.__y += dy

    # методи за достъп до данните

    def set_x(self, x):
        assert x >= 0, f'negative values for x not supported ({x})'
        self.__x = x

    def get_x(self):
        return self.__x

    # def set_visible(self, visible):
    #     self.__visible = visible

    # def is_visible(self):
    #     return self.__visible

if __name__ == '__main__':
    # 2. създаване на обект от дадения тип
    # клас -> Point, обект -> екземпляр, представител на класа p1
    p1 = Point() 
    p2 = Point(x = 30, y = 40)

    # p3 = Point(x = -2, y = 10)
    p2.draw()

    print('---')