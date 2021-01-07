class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        record={}
        ret=0
        start=0
        for i,item in enumerate(s,0):
            if item in record:
                end=record[item]
                while start<=end:
                    del record[s[start]]
                    start+=1
            ret=max(ret,i-start+1)
            record[item]=i
        return ret