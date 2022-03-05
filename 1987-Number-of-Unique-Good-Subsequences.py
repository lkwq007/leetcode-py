class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        term=10**9
        prev=0
        ret=0
        for item in binary:
            if item=="0":
                ret+=prev
            else:
                prev+=1
                ret+=prev
            ret%=term
        return ret