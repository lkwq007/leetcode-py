class Solution:
    def splitString(self, s: str) -> bool:
        def probe(start,last):
            if start==len(s):
                return True
            for idx in range(start+1,len(s)+1):
                if int(s[start:idx])+1==last:
                    if probe(idx,last-1):
                        return True
            return False
        for i in range(1,len(s)):
            if probe(i,int(s[:i])):
                return True
        return False