class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        # binary index tree?
        # or segments
        # or reverse order
        total=len(light)
        left_seg=[-1]*total
        right_seg=[-1]*total
        ret=0
        for i in range(total):
            idx=light[i]-1
            left_seg[idx]=idx
            right_seg[idx]=idx
            if idx>0 and left_seg[idx-1]!=-1:
                leftmost=left_seg[idx-1]
            else:
                leftmost=idx
            if idx<total-1 and right_seg[idx+1]!=-1:
                rightmost=right_seg[idx+1]
            else:
                rightmost=idx
            left_seg[rightmost]=leftmost
            right_seg[leftmost]=rightmost
            left_seg[idx]=leftmost
            right_seg[idx]=rightmost
            if leftmost==0 and rightmost==i:
                ret+=1
        return ret

class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        max_idx=-1
        ret=0
        for i in range(len(light)):
            idx=light[i]-1
            max_idx=max(max_idx,idx)
            if max_idx==i:
                ret+=1
        return ret