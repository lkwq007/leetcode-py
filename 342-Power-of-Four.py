class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        # signed 32 bit
        # use magic number 
        return num>0 and (num&(num-1))==0 and (715827882&num)==0