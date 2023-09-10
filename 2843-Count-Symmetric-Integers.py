class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ret=0
        for i in range(low,high+1):
            if len(str(i))%2:
                continue
            total=len(str(i))
            left=sum(map(int,str(i)[:total//2]))
            right=sum(map(int,str(i)[total//2:]))
            if left==right:
                ret+=1
        return ret