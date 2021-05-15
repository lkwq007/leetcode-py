class Solution:
    def isNumber(self, s: str) -> bool:
        def decimal(x):
            if len(x)<1:
                return False
            idx=1 if x[0] in "+-" else 0
            lst=x[idx:].split(".")
            if len(lst)==2:
                left=lst[0].isdigit() or len(lst[0])<1
                right=lst[1].isdigit() or len(lst[1])<1
                return (lst[0].isdigit() and right) or (left and lst[1].isdigit())
            return False
        def integer(x):
            if len(x)<1:
                return False
            idx=1 if x[0] in "+-" else 0
            return x[idx:].isdigit()
        s=s.lower()
        if "e" in s:
            lst=s.split("e")
            if len(lst)==2:
                return (decimal(lst[0]) or integer(lst[0])) and integer(lst[1])
        else:
            return decimal(s) or integer(s)
        return False