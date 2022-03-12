class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        # sum(paths[i].length) <= 10^5
        # binary search?
        left=0
        right=min(map(len,paths))
        def check(x):
            if x==0:
                return True
            
            return False
        while left<right:
            middle=left+(right-left)//2
            if check(middle):
                left=middle+1
            else:
                right=middle
        if check(left):
            return left
        return left-1