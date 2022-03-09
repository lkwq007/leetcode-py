class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        term=10**9+7
        zero=0
        one=0
        extra=0
        if "0" in binary:
            extra=1
        for i in range(len(binary)):
            item=binary[i]
            if item=="0":
                zero=zero+one
                zero%=term
            else:
                one=one+zero+1
                one%=term
        return (zero+one+extra)%term