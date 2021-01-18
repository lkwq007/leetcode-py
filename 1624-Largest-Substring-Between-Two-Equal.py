class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        record={}
        ret=-1
        for i,item in enumerate(s,0):
            if item not in record:
                record[item]=i
            else:
                ret=max(ret,i-record[item]-1)
        return ret