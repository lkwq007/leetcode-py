class Solution:
    def thousandSeparator(self, n: int) -> str:
        lst=str(n)
        ret=[]
        cnt=0
        for item in reversed(lst):
            cnt+=1
            ret.append(item)
            if cnt==3:
                ret.append(".")
                cnt=0
        if ret[-1]==".":
            ret[-1]=""
        return "".join(ret[::-1])