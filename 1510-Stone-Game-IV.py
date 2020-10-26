import functools
from math import sqrt
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @functools.lru_cache(maxsize=None)
        def judge(x):
            tmp=int(sqrt(x))
            if tmp*tmp==x:
                return True
            for i in range(tmp,0,-1):
                if not judge(x-i*i):
                    return True
            return False
        return judge(n)