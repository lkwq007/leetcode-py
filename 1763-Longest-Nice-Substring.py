class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ret=""
        def isNice(start,end):
            record={}
            for i in range(start,end+1):
                record[s[i]]=1
            for k in record:
                if k.lower() in record and k.upper() in record:
                    continue
                return False
            return True
        # brute force
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if isNice(i,j) and j-i+1>len(ret):
                    ret=s[i:j+1]
        return ret

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if not s:
            return ""
        record=set(s)
        for i in range(len(s)):
            if s[i].swapcase() not in record:
                s1=self.longestNiceSubstring(s[:i])
                s2=self.longestNiceSubstring(s[i+1:])
                return max(s1,s2,key=len)
        return s