# 1. дефиниция на класа
#  
# 1. без __init__.py
# import draw.point as dp

# from draw.point import Point


# 2. с __init__.py
# import draw as d
from draw import Point

if __name__ == '__main__':

    p1 = Point(x = 10, y = 20)
    
    p1.draw()

    print('---')