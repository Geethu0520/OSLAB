nj=int(input("Enter the number of jobs: "))
s=[]
for i in range(nj):
    a=int(input(f"Enter the execution time of job{i+1}: "))
    s.append(a)
s.sort()
t=0
wt=[]
for i in range(nj):
    wt.append(t)
    t+=s[i]
print("Job no\t Execution time\t Waiting time\t Turn around time")
for i in range(nj):
    print(f"J{i}\t\t",s[i],"\t\t",wt[i],"\t\t",wt[i]+s[i])
awt=sum(wt)/len(wt)
print("Average waiting time=",awt)
att=(sum(wt)+wt[-1]+s[-1])/len(wt)
print("Average turn around time=",att)
