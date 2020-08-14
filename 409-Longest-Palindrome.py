class Solution:
    def longestPalindrome(self, s: str) -> int:
        record={}
        for item in s:
            record[item]=record.get(item,0)+1
        odd=0
        ret=0
        for val in record.values():
            if val%2==0:
                ret+=val
            else:
                odd+=1
                ret+=val-1
        rest=1 if odd else 0
        return ret+rest