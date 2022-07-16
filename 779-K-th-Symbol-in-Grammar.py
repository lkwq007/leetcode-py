class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:
            return 0
        idx=(k-1)//2
        prev=self.kthGrammar(n-1,idx+1)
        if (k-1)%2:
            return 1-prev
        return prev