class Solution:
    def myAtoi(self, s: str) -> int:
        idx=0
        ret=0
        acc=0
        while idx<len(s) and s[idx]==" ":
            idx+=1
        if idx>=len(s) or not (s[idx].isdigit() or s[idx] in "+-"):
            return 0
        if s[idx] in "+-" and (idx+1<len(s) and s[idx+1].isdigit()):
            sign=-1 if s[idx]=="-" else 1
            idx+=1
            while idx<len(s) and s[idx].isdigit():
                acc=acc*10+int(s[idx])
                idx+=1
            if sign==-1:
                acc=-acc
        elif s[idx].isdigit():
            while idx<len(s) and s[idx].isdigit():
                acc=acc*10+int(s[idx])
                idx+=1
        return min(max(acc,-(2**31)),2**32-1)