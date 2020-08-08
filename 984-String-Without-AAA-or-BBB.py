class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        ret=[]
        last="b" if A>B else "a"
        while A>0 and B>0:
            if A>B:
                if last=="a":
                    ret.append("baa")
                else:
                    ret.append("aab")
                A-=2
                B-=1
            elif B>A:
                if last=="a":
                    ret.append("bba")
                else:
                    ret.append("abb")
                A-=1
                B-=2
            else:
                if last=="a":
                    ret.append("ba")
                else:
                    ret.append("ab")
                A-=1
                B-=1
        if A>0:
            ret.append("a"*A)
        if B>0:
            ret.append("b"*B)
        return "".join(ret)
