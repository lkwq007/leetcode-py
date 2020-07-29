# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left=1
        right=n
        while left<right:
            middle=left+(right-left)//2
            ret=guess(middle)
            if ret==0:
                return middle
            elif ret<0:
                right=middle
            else:
                left=middle+1
        return left