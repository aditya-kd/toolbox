def leastInterval(tasks, n: int) -> int:
        mp={}
        for item in tasks:
            mp[item]= mp.get(item, 0)+1
        # mp.sort(reverse=True, key=lambda x: x[1])
        values= sorted(mp.values(), reverse=True)     
        print(values)
        
        max_freq= values[-1]
        idle_time= (max_freq-1)*n
        i=len(values)-2
        while i>=0 and idle_time>0:
            idle_time = min(values[i], max_freq-1)
            i-=1

        idle_time = max(0, idle_time)
        return len(tasks)+idle_time






tasks = ["A","A","A","B","B","B"]
n= 2
tasks=["A","A","A","A","A","A","B","C","D","E","F","G"]
n=2
        
print(leastInterval(tasks, n))