class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s)<1 or s[0]=="0":
            return 0
        item=10**9+7
        dp=[0]*2
        last=0
        dp[-1]=1
        for item in s:
            digit=-1 if item=="*" else int(item)
            if digit==0 and last==0:
                return 0
            if digit>=0 and 10<=(last*10+digit)<=26:
                if digit==0:
                    now=dp[-2]
                else:
                    now=dp[-2]+dp[-1]
            elif digit0: