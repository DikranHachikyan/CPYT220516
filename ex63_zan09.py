# 1. дефиниция на класа
#  
class Point:
    
    def __init__(self, *, x=0, y=0):
        print('--- init obj ---')
        # данни на обекта
        self.__x = x
        self.__y = y

    # методи на обекта
    def draw(self):
        print(f'draw point at ({self.__x}, {self.__y} )')


    def move_to(self, dx, dy):
        self.__x += dx
        self.__y += dy


if __name__ == '__main__':
    # 2. създаване на обект от дадения тип
    # клас -> Point, обект -> екземпляр, представител на класа p1
    p1 = Point() 
    p2 = Point(x=30, y=40)

    # print(f'p2 x:({p2.__x})')
    # p2.__x = -1
    p2.draw()

    print('---')