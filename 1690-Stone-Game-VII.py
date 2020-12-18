class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        total=sum(stones)
        import functools
        @functools.lru_cache(maxsize=None)
        def play()