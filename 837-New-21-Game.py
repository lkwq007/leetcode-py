class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        # brute force
        dp=[0 for i in range(N)]
        for i in range(K):
            