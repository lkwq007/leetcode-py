class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words=str.split()
        mapping={}
        imapping={}
        if len(pattern)!=len(words):
            return False
        for i in range(len(pattern)):
            x=pattern[i]
            y=words[i]
            if x in mapping:
                if mapping[x]!=y:
                    return False
            else:
                mapping[x]=y
            if y in imapping:
                if imapping[y]!=x:
                    return False
            else:
                imapping[y]=x
        return True