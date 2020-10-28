import functools
class Solution:
    def minDays(self, n: int) -> int:
        @functools.lru_cache(maxsize=None)
        def eat(x):
            if x<4:
                return min(x,2)
            return 1+min(x%3+eat(x//3),x%2+eat(x//2))
        return eat(n)