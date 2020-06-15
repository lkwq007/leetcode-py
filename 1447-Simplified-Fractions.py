import functools
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        if n<2:
            return []
        @functools.lru_cache(maxsize=None)
        def gcd(a,b):
            if a==b:
                return a
            elif a>b:
                return gcd(min(a-b,b),max(a-b,b))
            else:
                return gcd(min(a,b-a),max(a,b-a))
        ret=[]
        for den in range(2,n+1):
            ret.append("1/"+str(den))
            for num in range(2,den):
                if num%2==0 and den%2==0 or num%den==0:
                    continue
                if gcd(num,den)==1:
                    ret.append(str(num)+"/"+str(den))
        return ret
