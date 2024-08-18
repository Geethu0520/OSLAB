def main():
    n = int(input("Enter the number of processes: "))
    p = list(range(n))
    bt = []
    pri = []
    wt = [0] * n
    tat = [0] * n

    for i in range(n):
        burst_time = int(input(f"Enter the Burst Time of Process {i}: "))
        priority = int(input(f"Enter the Priority of Process {i}: "))
        bt.append(burst_time)
        pri.append(priority)

    # Sorting processes based on priority
    for i in range(n):
        for k in range(i + 1, n):
            if pri[i] > pri[k]:
                p[i], p[k] = p[k], p[i]
                bt[i], bt[k] = bt[k], bt[i]
                pri[i], pri[k] = pri[k], pri[i]

    wtavg = wt[0] = 0
    tatavg = tat[0] = bt[0]

    for i in range(1, n):
        wt[i] = wt[i - 1] + bt[i - 1]
        tat[i] = tat[i - 1] + bt[i]
        wtavg += wt[i]
        tatavg += tat[i]

    print("\nPROCESS\tPRIORITY\tBURST TIME\tWAITING TIME\tTURNAROUND TIME")
    for i in range(n):
        print(f"{p[i]}\t\t{pri[i]}\t\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}")

    print("\nAverage Waiting Time is ---", wtavg / n)
    print("Average Turnaround Time is ---", tatavg / n)

if __name__ == "__main__":
    main()
