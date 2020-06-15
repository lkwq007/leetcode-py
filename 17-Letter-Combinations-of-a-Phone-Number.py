from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping={}
        base=ord("a")
        for i in range(2,10):
            tmp=""
            num=4 if i==7 or i==9 else 3
            for k in range(0,num):
                tmp+=chr(base)
                base+=1
            mapping[str(i)]=tmp
        ret=[]
        def combine(digit, buf):
            if len(digit)>0:
                tmp=digit[1:]
                for item in mapping[digit[0]]:
                    combine(tmp,buf+item)
            else:
                if buf:
                    ret.append(buf)
        combine(digits,"")
        return ret


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping={}
        base=ord("a")
        for i in range(2,10):
            tmp=""
            num=4 if i==7 or i==9 else 3
            for k in range(0,num):
                tmp+=chr(base)
                base+=1
            mapping[str(i)]=tmp
        def combine(digit):
            if len(digit)>1:
                ret=[]
                rest=combine(digit[1:])
                for hd in mapping[digit[0]]:
                    for tl in rest:
                        ret.append(hd+tl)
                return ret
            elif len(digit)==1:
                return list(mapping[digit])
            else:
                return []
        return combine(digits)

x=Solution()
print(x.letterCombinations("23"))
print(x.letterCombinations("2"))
print(x.letterCombinations(""))