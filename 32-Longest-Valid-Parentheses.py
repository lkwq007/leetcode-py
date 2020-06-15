class Solution:
    def longestValidParentheses(self, s: str) -> int:
        balance=0
        record={}
        max_val=0
        record[0]=-1
        for idx in range(0,len(s)):
            if s[idx]=="(":
                balance+=1
            elif balance>0:
                balance-=1
                if balance in record:
                    max_val=max(idx-record[balance],max_val)
                else:
                    record[balance]=idx     
        return max_val