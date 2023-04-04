class Solution:
    def partitionString(self, s: str) -> int:
        ret=1
        record={}
        last=0
        for i in range(len(s)):
            item=s[i]
            if record.get(item,-1)>=last:
                last=i
                ret+=1
            record[item]=i
        return ret