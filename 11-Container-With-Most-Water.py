class Solution:
    def maxArea(self, height: List[int]) -> int:
        # O(N)
        left=0
        right=len(height)-1
        ret=0
        while left<right:
            ret=max(ret,min(height[left],height[right])*(right-left))
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return ret

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # brute force TLE
        ret=0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                ret=max(ret,min(height[j],height[i])*(j-i))
        return ret