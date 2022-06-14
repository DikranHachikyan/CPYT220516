# 1. дефиниция на класа
#  
class Point:
    
    def __init__(self):
        print('--- init obj ---')
        # данни на обекта
        self.x = 10
        self.y = 20

    # методи на обекта
    def draw(self):
        print(f'draw point at ({self.x}, {self.y} )')

if __name__ == '__main__':
    # 2. създаване на обект от дадения тип
    # клас -> Point, обект -> екземпляр, представител на класа p1
    p1 = Point() 

    p1.draw()

    p1.x = 15
    p1.y = 6

    p1.draw()

    print('---')