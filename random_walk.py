
# 此实例模拟随机漫步
from random import choice

class RandomWalk():
    def __init__(self,num_points=5000):
        '''初始化随机漫步的属性'''
        self.num_points = num_points

        # 所有随机漫步都始于(0,0)
        self.x_value = [0]
        self.y_value = [0]
    
    
