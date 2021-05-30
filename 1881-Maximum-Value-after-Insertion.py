class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0]=="-":
            idx=1
            while idx<len(n):
                if x<int(n[idx]):
                    break
                idx+=1
        else:
            idx=0
            while idx<len(n):
                if x>int(n[idx]):
                    break
                idx+=1
        return n[:idx]+str(x)+n[idx:]