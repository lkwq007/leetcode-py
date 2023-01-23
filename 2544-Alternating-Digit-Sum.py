class Solution:
    def alternateDigitSum(self, n: int) -> int:
        acc=[0,0]
        flag=0
        while n>0:
            acc[flag]+=n%10
            n//=10
            flag=1-flag
        return (acc[0]-acc[1]) if flag else (acc[1]-acc[0])