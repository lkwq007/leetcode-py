import functools
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        if amount<coins[-1]:
            return -1
        @functools.lru_cache(maxsize=None)
        def local_change(amount,pos):
            