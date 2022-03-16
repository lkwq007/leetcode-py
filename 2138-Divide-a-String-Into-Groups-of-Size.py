class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ret=[]
        for i in range(0,len(s),k):
            ret.append(s[i:i+k])
        last=len(s)%k
        if last!=0:
            ret[-1]+=fill*(k-last)
        return ret