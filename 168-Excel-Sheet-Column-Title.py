class Solution:
    def convertToTitle(self, n: int) -> str:
        if n<27:
            return chr(64+n)
        cur=n%26
        if cur==0:
            return self.convertToTitle((n-1)//26)+"Z"
        return self.convertToTitle(n//26)+chr(64+cur)