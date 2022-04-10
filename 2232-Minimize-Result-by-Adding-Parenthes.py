class Solution:
    def minimizeResult(self, expression: str) -> str:
        # 3 <= expression.length <= 10
        left,right=expression.split("+")
        minval=int(left)+int(right)
        ret="("+expression+")"
        for i in range(len(left)):
            l0=left[:i]
            l1=left[i:]
            l0=1 if len(l0)==0 else int(l0)
            l1=0 if len(l1)==0 else int(l1)
            for j in range(1,len(right)+1):
                r0=right[:j]
                r1=right[j:]
                r0=0 if len(r0)==0 else int(r0)
                r1=1 if len(r1)==0 else int(r1)
                cur=l0*(l1+r0)*r1
                if cur<minval:
                    minval=cur
                    ret=left[:i]+"("+left[i:]+"+"+right[:j]+")"+right[j:]
        return ret