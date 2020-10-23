class Solution:
    def maxDepth(self, s: str) -> int:
        # input is VPS
        if len(s)<1:
            return 0
        self.idx=0
        total=len(s)
        def parse():
            ret=0
            while self.idx<total:
                if s[self.idx]=="(":
                    self.idx+=1
                    ret=max(1+parse(),ret)
                elif s[self.idx]==")":
                    self.idx+=1
                    return ret
                else:
                    self.idx+=1
            return ret
        return parse()