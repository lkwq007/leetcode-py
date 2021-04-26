class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        ret=0
        record={}
        lst="aeiouu"
        for i in range(len(lst)-1):
            record[lst[i]]=lst[i]+lst[i+1]
        acc=0
        last="u"
        for item in word:
            if item in record[last] and acc>0:
                acc+=1
                if item=="u":
                    ret=max(ret,acc)
            elif item=="a":
                acc=1
            else:
                acc=0
            last=item
        return ret