class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # 1 <= expression.length <= 20
        lst=[]
        acc=""
        for item in expression:
            if item in "+-*":
                lst.append(int(acc))
                lst.append(item)
                acc=""
            else:
                acc+=item
        if acc:
            lst.append(int(acc))
        mapping={"+": lambda a,b:a+b,
        "-": lambda a,b:a-b,
        "*": lambda a,b:a*b}
        import itertools
        def probe(expr):
            if len(expr)==1:
                return [expr[0]]
            ret=[]
            for i in range(1,len(expr),2):
                left=probe(expr[:i])
                right=probe(expr[i+1:])
                func=mapping[expr[i]]
                for l,r in itertools.product(left,right):
                    ret.append(func(l,r))
            return ret
        return probe(lst)