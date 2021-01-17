class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_len=max(map(min,rectangles))
        cnt=0
        for item in rectangles:
            if min(item)==max_len:
                cnt+=1
        return cnt