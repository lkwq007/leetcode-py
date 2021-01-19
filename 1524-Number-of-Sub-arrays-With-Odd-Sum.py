class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        term=10**9+7
        record=[0]*2
        record[0]=1
        acc=0
        ret=0
        for item in arr:
            acc+=item
            ret+=record[1-acc&1]
            ret%=term
            record[acc&1]+=1
        return ret
