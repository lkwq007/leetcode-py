class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        def to_complex(s):
            lst=s.split("+")
            return int(lst[0]),int(lst[1][:-1])
        a1,a2=to_complex(a)
        b1,b2=to_complex(b)
        return str(a1*b1-a2*b2)+"+"+str(a1*b2+a2*b1)+"i"