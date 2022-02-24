class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        prefix=[0]*(len(beans)+1)
        for i in range(len(beans)):
            prefix[i]=prefix[i-1]+beans[i]
        ret=prefix[-2]
        for i in range(len(beans)):
            total=len(beans)-i
            ret=min(ret,prefix[-2]-prefix[i-1]-total*beans[i]+prefix[i-1])
        return ret

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        total=sum(beans)
        ret=total
        for i in range(len(beans)):
            ret=min(ret,total-(len(beans)-i)*beans[i])
        return ret