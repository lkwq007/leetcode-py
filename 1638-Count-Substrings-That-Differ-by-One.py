class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        record={}
        for i in range(len(t)+1):
            for j in range(i):
                word=t[j:i]
                for k in range(len(word)):
                    tmp=word[:k]+"?"+word[(k+1):]
                    if tmp not in record:
                        record[tmp]={}
                    record[tmp][word]=record[tmp].get(word,0)+1
        ret=0
        for i in range(len(s)+1):
            for j in range(i):
                word=s[j:i]
                for k in range(len(word)):
                    tmp=word[:k]+"?"+word[(k+1):]
                    if tmp in record:
                        for k,v in record[tmp].items():
                            if k!=word:
                                ret+=v
        return ret
        