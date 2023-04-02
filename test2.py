from Algorithm import Multi_machine_scheduling1,Multi_machine_scheduling2,DFS
import  Algorithm
import random
import time
import matplotlib.pyplot as plt
import math

def test_2():
    global best_time  # 声明best_time为全局变量，后续函数可以直接使用并修改该变量
    global step  # 声明step为全局变量，后续函数可以直接使用并修改该变量
    A_Solution_time = []  # 定义一个空列表，用于记录贪心算法1的运行时间
    B_Solution_time = []  # 定义一个空列表，用于记录贪心算法2的运行时间
    A_Step = []
    B_Step = []
    M = 10  # 设定10个机器
    for N in range(1000, 10001, 1000):  # 循环遍历1000到10000中的每一千个任务数
        Time = [random.randint(1, 1000) for _ in range(N)]  # 随机生成N个任务的运行时间
        Algorithm.step = 0
        T3 = time.perf_counter()  # 记录开始时间
        G1 = Multi_machine_scheduling1(M, N, Time)  # 使用贪心算法1求解多机调度问题
        T4 = time.perf_counter()  # 记录结束时间
        A_Solution_time.append((T4 - T3) * 1000)  # 将该次运行时间添加到A_Solution_time列表中
        A_Step.append(Algorithm.step)

        Algorithm.step = 0
        T3 = time.perf_counter()  # 记录开始时间
        G2 = Multi_machine_scheduling2(M, N, Time)  # 使用贪心算法2求解多机调度问题
        T4 = time.perf_counter()  # 记录结束时间
        B_Solution_time.append((T4 - T3) * 1000)  # 将该次运行时间添加到B_Solution_time列表中
        B_Step.append(Algorithm.step)

    #绘制时间曲线
    x = [i for i in range(1000, 10001, 1000)]  # 生成一个从1000到10000中的每一千个任务数的列表，作为x轴上的坐标值
    plt.plot(x, A_Solution_time, 'ro-', label='Greedy 1')  # 绘制贪心算法1的运行时间折线图，颜色为红色，样式为实线，数据点用圆圈标识
    plt.plot(x, B_Solution_time, 'bo-', label='Greedy 2')  # 绘制贪心算法2的运行时间折线图，颜色为蓝色，样式为实线，数据点用圆圈标识
    plt.xlabel('N')  # 设置x轴标签为N
    plt.ylabel('Time(ms)')  # 设置y轴标签为Time(ms)
    plt.grid(True)  # 显示网格线
    plt.legend()  # 显示图例
    plt.title('The elapsed time of greedy algorithm(M = 10)')  # 设置标题为"The elapsed time of greedy algorithm(M = 10)"
    plt.show()  # 展示绘制的图形

    #绘制关键步骤曲线
    y1 = [M * x * 10 ** (-1) * 1.95  for x in range(1000, 10001, 1000)]
    plt.plot(x,A_Step,'ro-',label='Greedy 1')
    plt.plot(x,y1,'yo-',label='The theoretical value of greedy 1')
    y2 = [M * x * 10**(-1) * 1.2 for x in range(1000, 10001, 1000)]
    plt.plot(x, B_Step, 'bo-', label='Greedy 2')
    plt.plot(x, y2, 'mo-', label='The theoretical value of greedy 2')
    plt.xlabel('N')  # 设置x轴标签为N
    plt.ylabel('Committed step(times)')  # 设置y轴标签为Committed step(ms)
    plt.grid(True)  # 显示网格线
    plt.legend()  # 显示图例
    plt.title('The committed step of greedy algorithm(M = 10)')  # 设置标题为"The committed step of greedy algorithm(M = 10)"
    plt.show()  # 展示绘制的图形

    N = 500  # 设定任务数为500
    A_Solution_time = []  # 定义一个空列表，用于记录贪心算法1的运行时间
    B_Solution_time = []  # 定义一个空列表，用于记录贪心算法2的运行时间
    A_Step = []
    B_Step = []
    for M in range(10, 501, 50):  # 循环遍历从10到500中每50个机器数
        Time = [random.randint(1, 1000) for _ in range(N)]  # 随机生成N个任务的运行时间
        Algorithm.step = 0
        T3 = time.perf_counter()  # 记录开始时间
        G1 = Multi_machine_scheduling1(M, N, Time)  # 使用贪心算法1求解多机调度问题
        T4 = time.perf_counter()  # 记录结束时间
        A_Solution_time.append((T4 - T3) * 1000)  # 将该次运行时间添加到A_Solution_time列表中
        A_Step.append(Algorithm.step)

        T3 = time.perf_counter()  # 记录开始时间
        Algorithm.step = 0
        G2 = Multi_machine_scheduling2(M, N, Time)  # 使用贪心算法2求解多机调度问题
        T4 = time.perf_counter()  # 记录结束时间
        B_Solution_time.append((T4 - T3) * 1000)  # 将该次运行时间添加到B_Solution_time列表中
        B_Step.append(Algorithm.step)

    x = [i for i in range(10, 501, 50)]  # 生成一个从10到500中每50个机器数的列表，作为x轴上的坐标值
    plt.plot(x, A_Solution_time, 'ro-', label='Greedy 1')  # 绘制贪心算法1的运行时间折线图，颜色为红色，样式为实线，数据点用圆圈标识
    plt.plot(x, B_Solution_time, 'bo-', label='Greedy 2')  # 绘制贪心算法2的运行时间折线图，颜色为蓝色，样式为实线，数据点用圆圈标识
    plt.xlabel('M')  # 设置x轴标签为M
    plt.ylabel('Time(ms)')  # 设置y轴标签为Time(ms)
    plt.grid(True)  # 显示网格线
    plt.legend()  # 显示图例
    plt.title('The elapsed time of greedy algorithm(N = 500)')  # 设置标题为"The elapsed time of greedy algorithm(N = 500)"
    plt.show()  # 展示绘制的图形

    # 绘制关键步骤曲线
    plt.plot(x, A_Step, 'ro-', label='Greedy 1')
    y1 = [x * N  * 10**(-2) * 1.01  for x in range(10, 501, 50)]
    plt.plot(x, y1, 'yo-', label='The theoretical value of greedy 1')
    plt.plot(x, B_Step, 'bo-', label='Greedy 2')
    y2 = [x * N  * 10**(-1) * 4.2  for x in range(10, 501, 50)]
    plt.plot(x, y2, 'mo-', label='The theoretical value of greedy 2')
    plt.xlabel('M')  # 设置x轴标签为M
    plt.ylabel('Committed step(times)')  # 设置y轴标签为Committed step(ms)
    plt.grid(True)  # 显示网格线
    plt.legend()  # 显示图例
    plt.title('The committed step of greedy algorithm(N = 500)')  # 设置标题为"The committed step of greedy algorithm(N = 500)"
    plt.show()  # 展示绘制的图形

    M = 3  # 设定机器数为3
    Algorithm.step = 0
    Committed_step = []  # 定义一个空列表，用于记录回溯算法中的已提交步骤数
    best_Solution_time = []  # 定义一个空列表，用于记录回溯算法的最优解运行时间
    for N in range(1, 16):  # 循环遍历从1到15中每个任务数
        Algorithm.best_time = float('inf')  # 将Algorithm类中的best_time属性初始化为无穷大，用于记录回溯算法得到的最优解
        Algorithm.step = 0
        machine_Time = [0 for _ in range(M)]  # 初始化一个长度为M的列表，表示每台机器上目前的总运行时间为0
        Time = [random.randint(1, 1000) for _ in range(N)]  # 随机生成N个任务的运行时间
        T3 = time.perf_counter()  # 记录开始时间
        DFS(0, machine_Time, Time, M, N)  # 使用回溯算法求解多机调度问题
        T4 = time.perf_counter()  # 记录结束时间
        best_Solution_time.append((T4 - T3) * 1000)  # 将该次运行时间添加到best_Solution_time列表中
        Committed_step.append(Algorithm.step)

    #绘制时间曲线图
    x = [i for i in range(1, 16)]  # 生成一个从1到15的列表，作为x轴上的坐标值
    plt.plot(x, best_Solution_time, 'ro-')  # 绘制回溯算法的最优解运行时间折线图，颜色为红色，样式为实线，数据点用圆圈标识
    plt.grid(True)  # 显示网格线
    plt.xlabel('N')  # 设置x轴标签为N
    plt.ylabel('Time(ms)')  # 设置y轴标签为Time(ms)
    plt.title('The elapsed time of backtrace algorithm(M = 3)')  # 设置标题为"The elapsed time of backtrace algorithm(M = 3)"
    plt.show()  # 展示绘制的图形

    #绘制关键步骤曲线图
    plt.plot(x,Committed_step,'ro-',label='Committed step')
    y = [M ** x * 10 **(-2) * 2.5 for x  in range(1, 16)]
    plt.plot(x,y,'yo-',label = 'The theoretical value of backtrace')
    plt.grid(True)  # 显示网格线
    plt.xlabel('N')  # 设置x轴标签为N
    plt.ylabel('Committed step(times)')  # 设置y轴标签为Committed step(times)
    plt.title('The committed step of backtrace algorithm(M = 3)')  # 设置标题为"The committed step of backtrace algorithm(M = 3)"
    plt.legend()
    plt.show()  # 展示绘制的图形

    N = 10  # 设定任务数为10
    best_Solution_time = []  # 定义一个空列表，用于记录回溯算法的最优解运行时间
    Committed_step = []  # 定义一个空列表，用于记录回溯算法中的已提交步骤数
    for M in range(1, 10):  # 循环遍历从1到9中每个机器数
        Algorithm.best_time = float('inf')  # 将Algorithm类中的best_time属性初始化为无穷大，用于记录回溯算法得到的最优解
        Algorithm.step = 0
        machine_Time = [0 for _ in range(M)]  # 初始化一个长度为M的列表，表示每台机器上目前的总运行时间为0
        Time = [random.randint(1, 1000) for _ in range(N)]  # 随机生成N个任务的运行时间
        T3 = time.perf_counter()  # 记录开始时间
        DFS(0, machine_Time, Time, M, N)  # 使用回溯算法求解多机调度问题
        T4 = time.perf_counter()  # 记录结束时间
        best_Solution_time.append((T4 - T3) * 1000)  # 将该次运行时间添加到best_Solution_time列表中
        Committed_step.append((Algorithm.step))

    # 绘制时间曲线图
    x = [i for i in range(1, 10)]  # 生成一个从1到9的列表，作为x轴上的坐标值
    plt.plot(x, best_Solution_time, 'ro-')  # 绘制回溯算法的最优解运行时间折线图，颜色为红色，样式为实线，数据点用圆圈标识
    plt.grid(True)  # 显示网格线
    plt.xlabel('M')  # 设置x轴标签为M
    plt.ylabel('Time(ms)')  # 设置y轴标签为Time(ms)
    plt.title(
        'The elapsed time of backtrace algorithm(N = 10)')  # 设置标题为"The elapsed time of backtrace algorithm(N = 10)"
    plt.show()  # 展示绘制的图形

    # 绘制关键步骤曲线图
    plt.plot(x, Committed_step, 'ro-', label='Committed step')
    y = [x ** N * 10 ** (-2)  for x in range(1, 10)]
    plt.plot(x, y, 'yo-', label='The theoretical value of backtrace')
    plt.grid(True)  # 显示网格线
    plt.xlabel('M')  # 设置x轴标签为M
    plt.ylabel('Committed step(times)')  # 设置y轴标签为Committed step(times)
    plt.title(
        'The committed step of backtrace algorithm(N = 10)')  # 设置标题为"The committed step of backtrace algorithm(N = 10)"
    plt.legend()
    plt.show()  # 展示绘制的图形