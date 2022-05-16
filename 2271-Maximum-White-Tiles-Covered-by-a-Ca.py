class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        # The tiles are non-overlapping
        def calc(lst):
            lst.sort()
            ret=0
            # aligin with left, right?
            right=0
            acc=0
            for i in range(len(lst)):
                cur=lst[i][0]
                right=max(right,i)
                while right<len(lst) and lst[right][0]<=cur+carpetLen-1:
                    acc+=min(cur+carpetLen-1-lst[right][0]+1,lst[right][1]-lst[right][0]+1)
                    right+=1
                right-=1
                ret=max(ret,acc)
                if right!=i:
                    acc-=min(cur+carpetLen-1-lst[right][0]+1,lst[right][1]-lst[right][0]+1)
                if cur+carpetLen-1>=lst[i][1]:
                    acc-=lst[i][1]-lst[i][0]+1
                else:
                    acc-=carpetLen
            return ret
        return max(calc(tiles),calc([[-r,-l] for l,r in tiles]))
