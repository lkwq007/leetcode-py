class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n<1:
            return [""]
        ret=[]
        import functools
        @functools.lru_cache(maxsize=None)
        def generate(num):
            if num==1:
                return ["()"]
            ret=[]
            for i in range(2,num//2+1):
                l1=generate(i)
                l2=generate(num-i)
                for item1 in l1:
                    for item2 in l2:
                        ret.append(item1+item2)
                        ret.append(item2+item1)
            lst=generate(num-1)
            for item in lst:
                ret.append("()"+item)
                ret.append(item+"()")
                ret.append("("+item+")")
            ret=list(set(ret))
            return ret
        return generate(n)