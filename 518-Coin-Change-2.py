import functools
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount==0:
            return 1
        if len(coins)<1 or amount<min(coins):
            return 0
        last=len(coins)-1
        @functools.lru_cache(maxsize=None)
        def local_change(amount,cur):
            val=coins[cur]
            if amount%val:
                ret=0
            else:
                ret=1
            if cur==last:
                return ret
            while amount>0:
                ret+=local_change(amount,cur+1)
                amount-=val
            return ret
        return local_change(amount,0)
