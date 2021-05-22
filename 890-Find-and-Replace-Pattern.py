class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ret=[]
        for word in words:
            mapping={}
            imapping={}
            flag=True
            for a,b in zip(word,pattern):
                if a not in mapping:
                    if b not in imapping:
                        mapping[a]=b
                        imapping[b]=a
                    else:
                        flag=False
                        break
                elif mapping[a]!=b:
                    flag=False
                    break
            if flag:
                ret.append(word)
        return ret