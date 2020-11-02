class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n==1:
            return 5
        last=[1]*5
        for i in range(n-1):
            cur=[0]*5
            for j in range(5):
                cur[j]=sum(last[:j+1])
            last=cur
        return sum(last)