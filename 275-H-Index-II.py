class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations)<1:
            return 0
        left=0
        right=len(citations)
        total=len(citations)
        while left<right:
            middle=left+(right-left)//2
            h=total-middle
            if citations[middle]>=h:
                right=middle
            else:
                left=middle+1
        return total-left
