class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.sort()
        restrictions.append([0,0])
        left=0
        right=n-1
        def check(val):
            return True
        while left<right:
            middle=left+(right-left)//2
            if check(middle):
                left=middle+1
            else:
                right=middle
        return left if check(left) else left-1