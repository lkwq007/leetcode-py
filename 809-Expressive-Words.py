class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def convert(x):
            ret=[[x[0],1]]
            for item in x[1:]:
                if item==ret[-1][0]:
                    ret[-1][1]+=1
                else:
                    ret.append([item,1])
            return ret
        acc=0
        ref=convert(s)
        for word in words:
            lst=convert(word)
            if len(lst)==len(ref):
                flag=True
                for (x,cnt0),(y,cnt1) in zip(lst,ref):
                    if x!=y or cnt0>cnt1 or (cnt0<cnt1 and cnt1<3):
                        flag=False
                        break
                if flag:
                    acc+=1
        return acc