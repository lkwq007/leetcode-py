class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        right=len(colors)-1
        while right>0:
            if colors[right]!=colors[0]:
                break
            right-=1
        left=0
        while left<len(colors):
            if colors[left]!=colors[-1]:
                break
            left+=1
        return max(len(colors)-left-1,right)