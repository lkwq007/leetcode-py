class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        lst=[a,b,c]
        lst.sort()
        ret=0
        while lst[1]>0:
            ret+=1
            lst[2]-=1
            lst[1]-=1
            lst.sort()
        return ret