class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        lst=[0]*26
        base=ord("A")
        for item in tasks:
            idx=ord(item)-base
            lst[idx]+=1
        last=[-n-1]*26
        pool=[i for i in range(26)]
        cnt=0
        total=len(tasks)
        tick=0
        while cnt<total:
            pool.sort(key=lambda x:-lst[x])
            min_idx=-1
            for pid in pool:
                if last[pid]+n<tick and lst[pid]>0:
                    last[pid]=tick
                    tick+=1
                    cnt+=1
                    min_idx=-1
                    lst[pid]-=1
                    break
                elif lst[pid]>0:
                    if min_idx==-1 or last[min_idx]>last[pid]:
                        min_idx=pid
            if min_idx!=-1:
                cnt+=1
                lst[min_idx]-=1
                acc=last[min_idx]+n
        return acc