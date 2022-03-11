class Solution:
    def longestAwesome(self, s: str) -> int:
        # s consists only of digits
        mask=1
        mapping={}
        pattern=[0]
        for i in range(10):
            mapping[i]=mask
            pattern.append(mask)
            mask=mask<<1
        record={}
        acc=0
        record[0]=-1
        ret=1
        for i in range(len(s)):
            item=int(s[i])
            acc=acc^mapping[item]
            for x in pattern:
                cur=x^acc
                if cur in record:
                    ret=max(ret,i-record[cur])
            if acc not in record:
                record[acc]=i
        return ret