class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left=0
        right=len(intervals)-1
        def search(l,r,target):
            left=l
            right=r
            while left<right:
                middle=left+(right-left)//2
                if intervals[middle][0]==target:
                    return middle
                elif intervals[middle][0]>target:
                    right=middle
                else:
                    left=middle+1
        start=search(0,len(intervals),newInterval[0])
        end=search(start,len(intervals),newInterval[1])
        if start>=len(intervals)
            