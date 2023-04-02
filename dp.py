import random
def multi_machine_scheduling(jobs, m):
    n = len(jobs)

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + jobs[j - 1]
    return dp[m][n]


if __name__ == '__main__':
    #m = int(input("Please input machine number:"))
    #n = int(input("Please input work number:"))
    m = 3
    n = 7
    if m > n :
        print("machine number has to greater than work number")
    work_time = [random.randint(1, 100) for _ in range(n)]
    work_time = [2, 5, 4, 7, 1, 3, 8]
    print("work time:", work_time)
    finish_time = multi_machine_scheduling( work_time,m)

    print("Finish Time:%s"%finish_time)
    input_tmp = input("press to exit")