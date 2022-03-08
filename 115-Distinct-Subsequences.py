class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s)<len(t):
            return 0
        template=[0]*(len(t)+1)
        dp=[template[:] for _ in range(len(s)+1)]
        for i in range(len())
