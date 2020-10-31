class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        last=-1
        ret=0
        for i in range(len(seats)):
            if seats[i]==1:
                if last==-1:
                    ret=max(ret,i)
                else:
                    dist=i-last
                    ret=max(ret,dist//2)
                last=i
        if seats[-1]==0:
            ret=max(ret,len(seats)-1-last)
        return ret
