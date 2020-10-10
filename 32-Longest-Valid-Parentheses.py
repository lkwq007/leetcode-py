class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ret=0
        balance=0
        record={}
        record[0]=-1
        for idx in range(len(s)):
            item=s[idx]
            if item==")":
                if balance>0:
                    balance-=1
                    if balance in record:
                        ret=max(ret,idx-record[balance])
                else:
                    balance=0
                    record={}
                    record[0]=idx
            else:
                balance+=1
                record[balance]=idx
        return ret


# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         balance=0
#         record={}
#         max_val=0
#         record[0]=-1
#         for idx in range(0,len(s)):
#             if s[idx]=="(":
#                 balance+=1
#             elif balance>0:
#                 balance-=1
#                 if balance in record:
#                     max_val=max(idx-record[balance],max_val)
#                 else:
#                     record[balance]=idx     
#         return max_val