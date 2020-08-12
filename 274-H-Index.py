class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        left=0
        right=len(citations)-1
        while left<right:
            middle=left+(right-left)//2
            cnt=len(citations)-middle
            if citations[middle]<cnt:
                left=middle+1
            else:
                right=middle
        while left<len(citations) and citations[left]<(len(citations)-left):
            left+=1
        return len(citations)-left