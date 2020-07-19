class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=a[::-1]
        b=b[::-1]
        if len(a)<len(b):
            a,b=b,a
        ret=[]
        carry=0
        for i in range(len(b)):
            total=int(a[i])+int(b[i])+carry
            if total>1:
                total-=2
                carry=1
            else:
                carry=0
            ret.append(str(total))
        for i in range(len(b),len(a)):
            total=int(a[i])+carry
            if total>1:
                total-=2
                carry=1
            else:
                carry=0
            ret.append(str(total))
        if carry:
            ret.append(str(carry))
        return "".join(reversed(ret))