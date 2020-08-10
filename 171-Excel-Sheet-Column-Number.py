class Solution:
    def titleToNumber(self, s: str) -> int:
        ret=0
        base=ord("A")-1
        for item in s:
            ret*=26
            ret+=ord(item)-base
        return ret