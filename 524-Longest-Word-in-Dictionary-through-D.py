class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        if len(s)<1:
            return ""
        ret=""
        for item in d:
            i=0
            j=0
            while i<len(item):
                while j<len(s) and s[j]!=item[i]:
                    j+=1
                if j<len(s):
                    i+=1
                    j+=1
                else:
                    break
            if len(ret)<0:
                ret=item
            if i==len(item) and (len(item)>len(ret) or (len(item)==len(ret) and item<ret)):
                ret=item
        return ret