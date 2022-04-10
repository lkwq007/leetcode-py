class Solution:
    def maxScore(self, nums: List[int]) -> int:
        def gcd(a,b):
            while b>0:
                a,b=b,a%b
            return a
        n=len(nums)//2
        mapping=[0]*len(nums)
        mask=1
        for i in range(len(mapping)):
            mapping[i]=mask
            mask=mask<<1
        import functools
        @functools.lru_cache(maxsize=None)
        def probe(acc,pos):
            if pos>=n:
                return 0
            ret=0
            for i in range(len(mapping)):
                if mapping[i]&acc==0:
                    for j in range(i+1,len(mapping)):
                        if mapping[j]&acc==0:
                            ret=max(probe(acc|mapping[i]|mapping[j],pos+1)+(pos+1)*gcd(nums[i],nums[j]),ret)
            return ret
        return probe(0,0)