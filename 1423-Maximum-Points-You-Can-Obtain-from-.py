from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k<1:
            return 0
        if k>=len(cardPoints):
            return sum(cardPoints)
        acc=0
        for i in range(k):
            acc+=cardPoints[i]
        max_val=acc
        for i in range(k-1,-1,-1):
            acc+=cardPoints[i-k]-cardPoints[i]
            max_val=max(max_val,acc)
        return max_val

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k<1:
            return 0
        if k>=len(cardPoints):
            return sum(cardPoints)
        template=[0]*(k+1)
        dp=[0]*(k+1)
        last=[0]*(k+1)
        for i in range(1,k+1):
            for j in range(i+1):
                if j==0:
                    dp[j]=last[j]+cardPoints[-i]
                elif j==i:
                    dp[j]=last[j-1]+cardPoints[j-1]
                else:
                    dp[j]=max(last[j-1]+cardPoints[j-1],last[j]+cardPoints[-(i-j)])
            tmp=dp
            dp=last
            last=tmp
        return max(last)
x=Solution()
print(x.maxScore([96,90,41,82,39,74,64,50,30],8))