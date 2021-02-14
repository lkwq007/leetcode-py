class Solution:
    def countHomogenous(self, s: str) -> int:
        term=10**9+7
        ret=0
        acc=0
        last=""
        for item in s:
            if last==item:
                acc+=1
            else:
                acc=1
            ret+=acc
            ret%=term
            last=item
        return ret