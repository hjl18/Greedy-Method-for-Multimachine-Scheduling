# Simulation of a GPU cluster online scheduling problem

# Import necessary libraries
import random
import numpy as np
import simpy

# Define the simulation environment
class GPUScheduler:
    def __init__(self, env, num_gpus):
        self.env = env
        self.num_gpus = num_gpus
        self.gpus = simpy.Resource(env, num_gpus)

    # Define a function to simulate a task
    def task(self, task_id, task_duration):
        yield self.env.timeout(task_duration)

    # Define a function to simulate a user
    def user(self, user_id, arrival_rate, task_duration):
        while True:
            yield self.env.timeout(random.expovariate(arrival_rate))
            task_id = f"User {user_id}'s task at {self.env.now}"
            print(f"{task_id} submitted at {self.env.now}")
            with self.gpus.request() as request:
                yield request
                print(f"{task_id} started at {self.env.now}")
                yield self.env.process(self.task(task_id, task_duration))
                print(f"{task_id} finished at {self.env.now}")

# Define a function to simulate the GPU cluster with a first-come, first-served scheduling policy
def fcfs_scheduler(env, num_gpus, arrival_rate, task_duration):
    gpu_scheduler = GPUScheduler(env, num_gpus)
    for i in range(10):
        env.process(gpu_scheduler.user(i, arrival_rate, task_duration))
    env.run()

# Define a function to simulate the GPU cluster with a shortest-job-first scheduling policy
def sjf_scheduler(env, num_gpus, arrival_rate, task_duration):
    gpu_scheduler = GPUScheduler(env, num_gpus)
    for i in range(10):
        env.process(gpu_scheduler.user(i, arrival_rate, task_duration))
    env.run()

# Define a function to simulate the GPU cluster with a round-robin scheduling policy
def rr_scheduler(env, num_gpus, arrival_rate, task_duration):
    gpu_scheduler = GPUScheduler(env, num_gpus)
    for i in range(10):
        env.process(gpu_scheduler.user(i, arrival_rate, task_duration))
    env.run()

# Set the simulation parameters
num_gpus = 4
arrival_rate = 0.5
task_duration = 10
env = simpy.Environment()



# Simulate the GPU cluster with a first-come, first-served scheduling policy
#fcfs_scheduler(env, num_gpus, arrival_rate, task_duration)



# Simulate the GPU cluster with a shortest-job-first scheduling policy
#sjf_scheduler(env, num_gpus, arrival_rate, task_duration)



# Simulate the GPU cluster with a round-robin scheduling policy
#rr_scheduler(env, num_gpus, arrival_rate, task_duration)

# The code above simulates the GPU cluster with three different scheduling policies: first-come, first-served, shortest-job-first, and round-robin.