class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        term=10**9+7
        hlst=[]
        vlst=[]
        horizontalCuts.append(h)
        verticalCuts.append(w)
        horizontalCuts.sort()
        verticalCuts.sort()
        last=0
        for item in horizontalCuts:
            diff=item-last
            hlst.append(diff)
            last=item
        last=0
        for item in verticalCuts:
            diff=item-last
            vlst.append(diff)
            last=item
        return max(hlst)*max(vlst)%term