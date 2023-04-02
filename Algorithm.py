import random
import time
import matplotlib.pyplot as plt

step = 0
best_time = float('inf')


def Multi_machine_scheduling1(M, N, Time):
    global step
    step = 0
    # 定义一个空列表，长度为M，表示每台机器目前的总运行时间为0
    machine_Time = []
    for i in range(M):
        machine_Time.append(0)

    # 循环遍历每个任务的运行时间
    for i in Time:
        # 找出目前所有机器中运行时间最短的机器
        min_Time = machine_Time[0]
        k = 0
        for j in range(M):
            if min_Time > machine_Time[j]:
                min_Time = machine_Time[j]
                k = j
                step += 1
        # 将该任务分配给运行时间最短的机器，并更新该机器的总运行时间
        machine_Time[k] += i

    # 返回所有机器中运行时间最长的值，即为贪心算法得到的最优解
    return max(machine_Time)


def Multi_machine_scheduling2(M, N, Time):
    global step
    # 将任务按照运行时间从大到小排序
    Time_Sorted = sorted(Time)
    Time_Sorted.reverse()

    # 定义一个空列表，长度为M，表示每台机器目前的总运行时间为0
    machine_Time = []
    for i in range(M):
        machine_Time.append(0)

    # 循环遍历每个任务的运行时间（按照从大到小的顺序）
    for i in Time_Sorted:
        # 找出目前所有机器中运行时间最短的机器
        min_Time = machine_Time[0]
        k = 0
        for j in range(M):
            if min_Time > machine_Time[j]:
                min_Time = machine_Time[j]
                k = j
                step += 1
        # 将该任务分配给运行时间最短的机器，并更新该机器的总运行时间
        machine_Time[k] += i

    # 返回所有机器中运行时间最长的值，即为贪心算法得到的最优解
    return max(machine_Time)


# 定义一个函数，用来比较当前各台机器的总运行时间，并返回其中最大值
def compare(M, machine_Time):
    tmp = 0
    for i in range(M):
        if machine_Time[i] > tmp:
            tmp = machine_Time[i]
    return tmp

# 定义一个深度优先搜索函数，用于遍历所有可能的任务分配方案，并更新best_time
def DFS(d, machine_Time, Time, M, N):
    global best_time  # 声明best_time为全局变量，方便在函数内部进行修改
    global step  # 声明step为全局变量，用于记录已提交的步骤数
    if d == N:  # 如果已经将所有任务都分配完毕
        tmp = compare(M, machine_Time)  # 比较之前各台机器的总运行时间，并返回其中最大值
        if tmp < best_time:  # 如果当前总完成时间比之前得到的最优解还要小
            step += 1  # 记录已提交的步骤数加1
            best_time = tmp  # 更新最优解
        return
    for i in range(M):  # 循环遍历每一台机器
        machine_Time[i] += Time[d]  # 将当前任务分配给第i台机器，并更新该机器的总运行时间
        if machine_Time[i] < best_time:  # 剪枝：如果当前所有机器的总运行时间还没有超过之前得到的最优解
            step += 1  # 记录已提交的步骤数加1
            DFS(d + 1, machine_Time, Time, M, N)  # 继续递归调用DFS函数，分配下一个任务
        machine_Time[i] -= Time[d]  # 回溯，将当前任务从第i台机器上取回，并恢复该机器的总运行时间


