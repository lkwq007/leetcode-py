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