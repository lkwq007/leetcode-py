class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ret=0
        import functools
        @functools.lru_cache(maxsize=None)
        def is_prime(x):
            if x<4:
                return True
            if x&1==0:
                return False
            i=3
            while i*i<=x:
                if x%i==0:
                    return False
                i+=2
            return True
        @functools.lru_cache(maxsize=None)
        def check(x):
            if x&1==0 and is_prime(x//2):
                return 1+2+x+x//2
            i=3
            while i*i<x:
                if x%i==0:
                    if is_prime(i) and is_prime(x//i) and x//i!=i:
                        return 1+x+x//i+i
                    elif is_prime(i) and i*i==x//i:
                        return 1+x+x//i+i
                    else:
                        return 0
                i+=2
            return 0
        for item in nums:
            if item==8:
                ret+=1+2+4+8
            elif item>5:
                ret+=check(item)
        return ret