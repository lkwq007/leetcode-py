class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        acc=0
        pool=[]
        for num,start,end in trips:
            pool.append((start,1,num))
            pool.append((end,0,num))
        pool.sort()
        for loc,state,num in pool:
            if state==0:
                acc-=num
            else:
                acc+=num
                if acc>capacity:
                    return False
        return True

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        acc=0
        pool=[]
        for num,start,end in trips:
            pool.append((start,num))
            pool.append((end,-num))
        pool.sort()
        for loc,num in pool:
            acc+=num
            if acc>capacity:
                return False
        return True

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        loc=[0]*1001
        for num,start,end in trips:
            loc[start]+=num
            loc[end]-=num
        acc=capacity
        for item in loc:
            acc-=item
            if acc<0:
                return False
        return True