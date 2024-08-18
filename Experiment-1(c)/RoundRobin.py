def findWaitingTime(processes, n, bt, wt, quantum):
    rem_bt = [0] * n
    for i in range(n):
        rem_bt[i] = bt[i]
    t = 0
    while (1):
        done = True
        for i in range(n):
            if rem_bt[i] > 0:
                done = False
                if rem_bt[i] > quantum:
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t = t + rem_bt[i]
                    wt[i] = t - bt[i]
                    rem_bt[i] = 0
        if done is True:
            break
def findTurnAroundTime(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def findavgTime(processes, n, bt, quantum):
    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0
    findWaitingTime(processes, n, bt, wt, quantum)
    findTurnAroundTime(processes, n, bt, wt, tat)
    print("Processes   Burst Time   Waiting Time   Turn-Around Time")
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" ", i + 1, "\t\t", bt[i], "\t\t", wt[i], "\t\t", tat[i])
    print("\nAverage waiting time = %.5f"%(total_wt / n))
    print("Average turn-around time = %.5f"%(total_tat / n))

if __name__ == "__main__":
    processes = [1, 2, 3, 4, 5, 6]
    n = len(processes)
    burst_time = [10, 5, 8, 3, 12, 6]
    quantum = 2
    findavgTime(processes, n, burst_time, quantum)
