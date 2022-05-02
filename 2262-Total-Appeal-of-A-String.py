class Solution:
    def appealSum(self, s: str) -> int:
        record={}
        ret=0
        # x to last idx
        last=0
        for i in range(len(s)):
            item=s[i]
            if item not in record:
                last+=i+1
                ret+=last
            else:
                last=last+i-record[item]
                ret+=last
            record[item]=i
        return ret

class Solution:
    def appealSum(self, s: str) -> int:
        record={}
        ret,last=0,0
        for i,item in enumerate(s):
            last+=i-record.get(item,-1)
            ret+=last
            record[item]=i
        return ret