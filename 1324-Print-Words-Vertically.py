class Solution:
    def printVertically(self, s: str) -> List[str]:
        words=s.split(" ")
        total=0
        for item in words:
            total=max(total,len(item))
        ret=["" for _ in range(total)]
        for i in range(len(words)):
            item=words[i]
            for j in range(len(item)):
                c=item[j]
                if len(ret[j])<i:
                    ret[j]+=" "*(i-len(ret[j]))
                ret[j]+=c
        return ret