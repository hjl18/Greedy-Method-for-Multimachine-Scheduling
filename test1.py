from Algorithm import Multi_machine_scheduling1,Multi_machine_scheduling2,DFS
import Algorithm
import random
import time
import matplotlib.pyplot as plt


def test():
    global best_time # 使用全局变量best_time
    M = 3 # 机器数
    N = 7 # 任务数
    Elapsed_time = []#运行时间列表
    Opt_solution = []#最优解列表
    A_opt_solution = []#贪心算法1近似最优解上限列表
    B_opt_solution = []#贪心算法2近似最优解上限列表
    for i in range(100): # 循环100次，生成不同的测试案例
        Time = [random.randint(1, 1000) for _ in range(N)] # 随机生成N个任务的运行时间
        Algorithm.best_time = float('inf') # 初始化Backtrace算法的最优解为正无穷
        machine_Time = [0 for _ in range(M)] # 初始化每个机器的完成时间为0
        T3 = time.perf_counter() # 记录开始时间
        G1 = Multi_machine_scheduling1(M,N,Time)#Greedy1算法求解
        T4 = time.perf_counter() # 记录结束时间
        A_opt_solution.append(G1) # 将贪心算法1得到的近似最优解上限添加到列表中
        Elapsed_time_G1 = (T4 - T3)*1000 # 计算算法运行耗时

        T3 = time.perf_counter() # 记录开始时间
        G2 = Multi_machine_scheduling2(M,N,Time)#Greedy2算法求解
        T4 = time.perf_counter() # 记录结束时间
        B_opt_solution.append(G2) # 将贪心算法2得到的近似最优解上限添加到列表中
        Elapsed_time_G2 = (T4 - T3)*1000 # 计算算法运行耗时

        T3 = time.perf_counter() # 记录开始时间
        DFS(0, machine_Time, Time,M,N)#Backtrace算法求解
        F = Algorithm.best_time # 获取算法得到的最优解
        T4 = time.perf_counter() # 记录结束时间
        Opt_solution.append(F) # 将最优解添加到列表中
        Elapsed_time_F = (T4 - T3)*1000 # 计算算法运行耗时

        Elapsed_time.append((Elapsed_time_G1,Elapsed_time_G2,Elapsed_time_F)) # 将三个算法的运行耗时添加到列表中

    return Opt_solution,A_opt_solution,B_opt_solution,Elapsed_time # 返回最优解和三种算法的近似最优解上限以及运行时间

def test_1():
    global best_time # 使用全局变量best_time
    P1 = [] # 贪心算法1得到的近似最优解等于最优解的概率列表
    P2 = [] # 贪心算法2得到的近似最优解等于最优解的概率列表
    for j in range(100): # 循环100次，生成不同的测试案例
        Opt_solution, A_opt_solution, B_opt_solution, Elapsed_time = test() # 调用test函数获取最优解和三种算法的近似最优解上限以及运行时间
        probability_1 = 0 # 初始化贪心算法1得到的近似最优解等于最优解的概率为0
        probability_2 = 0 # 初始化贪心算法2得到的近似最优解等于最优解的概率为0
        for i in range(len(Opt_solution)):
            if Opt_solution[i] == A_opt_solution[i]: # 如果贪心算法1得到的近似最优解等于最优解则累加计数器
                probability_1 += 1
            if Opt_solution[i] == B_opt_solution[i]: # 如果贪心算法2得到的近似最优解等于最优解则累加计数器
                probability_2 += 1
        probability_1 = probability_1 / len(A_opt_solution) # 计算贪心算法1得到的近似最优解等于最优解的概率
        probability_2 = probability_2 / len(B_opt_solution)  # 计算贪心算法2得到的近似最优解等于最优解的概率
        P1.append(probability_1)  # 将贪心算法1得到的近似最优解等于最优解的概率添加到列表中
        P2.append(probability_2)  # 将贪心算法2得到的近似最优解等于最优解的概率添加到列表中
    x = [i for i in range(100)]  # 定义x轴坐标为从0到99的整数
    plt.title('Probability distribution of optimal solution')  # 设置标题
    plt.plot(x, P1, 'ro-', label='Greedy 1')  # 绘制贪心算法1得到的近似最优解等于最优解的概率折线图
    plt.plot(x, P2, 'bo-', label='Greedy 2')  # 绘制贪心算法2得到的近似最优解等于最优解的概率折线图
    plt.xlabel('Group')  # 设置x轴标签
    plt.ylabel('Probability')  # 设置y轴标签
    plt.grid(True)  # 显示网格线
    plt.legend()  # 显示图例
    plt.show()  # 展示绘制的图像


