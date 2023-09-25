class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        total=len(s)
        one=0
        for item in s:
            if item=="1":
                one+=1
        return "1"*(one-1)+"0"*(total-one)+"1"