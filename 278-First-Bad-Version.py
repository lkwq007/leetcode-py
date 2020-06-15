# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return True
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # total n
        left=1
        right=n
        if isBadVersion(left):
            return left
        while left<right:
            middle=left+(right-left)//2
            if isBadVersion(middle):
                right=middle
            else:
                if left==middle:
                    left=right
                else:
                    left=middle
        return left