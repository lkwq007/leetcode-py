class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        left=1
        right=num
        while left<right:
            middle=left+(right-left)//2
            if middle*middle==num:
                return True
            if middle*middle>num:
                right=middle
            else:
                left=middle+1
        return left*left==num
