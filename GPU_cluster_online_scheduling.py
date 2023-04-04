import random
import numpy as np
import matplotlib.pyplot as plt
class Task:
    def __init__(self, submit_time, task_time):
        self.submit_time = submit_time
        self.task_time = task_time
class GPU:
    def __init__(self):
        self.finish_time = 0
def generate_task(lamda):
    submit_time = np.random.poisson(lamda)
    task_time = int(np.random.uniform(1, 10))
    return Task(submit_time, task_time)
def random_schedule(gpu_list, task):
    available_gpu_list = [gpu for gpu in gpu_list if gpu.finish_time <= task.submit_time]
    if available_gpu_list:
        selected_gpu_list = random.sample(available_gpu_list, random.randint(1, len(available_gpu_list)))
        finish_time = task.submit_time + task.task_time
        for gpu in selected_gpu_list:
            gpu.finish_time = finish_time / len(selected_gpu_list)
def greedy_schedule(gpu_list, task):
    available_gpu_list = [gpu for gpu in gpu_list if gpu.finish_time <= task.submit_time]
    if available_gpu_list:
        available_gpu_list.sort(key=lambda gpu: gpu.finish_time)
        selected_gpu_list = available_gpu_list[:random.randint(1, len(available_gpu_list))]
        finish_time = task.submit_time + task.task_time
        for gpu in selected_gpu_list:
            gpu.finish_time = finish_time / len(selected_gpu_list)
def simulate(schedule_func):
    m = 10
    gpu_list = [GPU() for _ in range(m)]
    task_list = [generate_task(3) for _ in range(num_tasks)]
    total_submit_time = 0
    total_task_time = 0
    for task in task_list:
        total_submit_time += task.submit_time
        total_task_time += task.task_time
        schedule_func(gpu_list, task)
    utilization = sum([gpu.finish_time for gpu in gpu_list if gpu.finish_time > 0]) / (len(gpu_list) * max([gpu.finish_time for gpu in gpu_list]))
    average_delay = (sum([gpu.finish_time - task.submit_time for gpu in gpu_list if gpu.finish_time > 0 for task in task_list if task.submit_time <= gpu.finish_time]) + total_task_time) / len(task_list)
    return utilization, average_delay
if __name__ == '__main__':
    # 设置模拟参数
    num_tasks = 1000
    max_time = 100
    # 随机调度策略
    random_utilization_list = []
    random_delay_list = []
    for lamda in range(1, max_time):
        utilization, delay = simulate(random_schedule)
        random_utilization_list.append(utilization)
        random_delay_list.append(delay)
    # 贪心调度策略
    greedy_utilization_list = []
    greedy_delay_list = []
    for lamda in range(1, max_time):
        utilization, delay = simulate(greedy_schedule)
        greedy_utilization_list.append(utilization)
        greedy_delay_list.append(delay)
    # 绘制图像
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1)
    plt.plot(range(1, max_time), random_utilization_list, label='Random')
    plt.plot(range(1, max_time), greedy_utilization_list, label='Greedy')
    plt.xlabel('Arrival rate (lamda)')
    plt.ylabel('Utilization')
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(range(1, max_time), random_delay_list, label='Random')
    plt.plot(range(1, max_time), greedy_delay_list, label='Greedy')
    plt.xlabel('Arrival rate (lamda)')
    plt.ylabel('Average delay')
    plt.legend()
    plt.show()
'''
if __name__ == "__main__":
    m = 4#The number of GPU cluster
    n = 1000#The number of assignment
    a1 = 0
    b1 = 10
    a2 = 20
    b2 = 30
    a3 = 40
    b3 = 50
    r = 3

    # The cost of assignment
    time1 = np.random.uniform(a1,b1,int(n * 0.3))#Low load
    time2 = np.random.uniform(a2,b2,int(n * 0.5))#Medium load
    time3 = np.random.uniform(a3,b3,int(n * 0.2))#High load
    time = np.concatenate((time1, time2))
    time = np.concatenate((time, time3))

    # The time of the assignment when students and teachers submit
    submit_time = poisson.rvs(mu = r, size = n)

    # Deadline
    require_finish_time = submit_time + time

    #TODO:schedule algorithm
'''

