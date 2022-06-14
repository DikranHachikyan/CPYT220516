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


if __name__ == '__main__':
    # 2. създаване на обект от дадения тип
    # клас -> Point, обект -> екземпляр, представител на класа p1
    p1 = Point() 
    p2 = Point(x=30, y=40)

    p1.draw()
    p2.draw()
    
    p2.move_to(-10, 5)

    p2.draw()

    print('---')