import random
import time
import matplotlib.pyplot as plt
import numpy as np
from test1 import test_1
from test2 import test_2
from Algorithm import best_time,step
import  Algorithm

if __name__ == "__main__":
    global best_time, step  # 在主函数中声明best_time和step为全局变量，方便在各个函数中进行修改
    test_1()  # 调用测试函数test_1()，对第一种贪心算法进行测试
    Algorithm.best_time = float('inf')  # 将Algorithm类中的best_time属性初始化为无穷大，用于记录回溯算法得到的最优解
    test_2()  # 调用测试函数test_2()，对回溯算法进行测试
