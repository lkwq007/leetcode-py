class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        # disjoint set
        total=len(arr)
        left=[-1]*total
        right=[-1]*total
        ret=-1
        cnt=0
        for i,idx in enumerate(arr,1):
            idx-=1
            leftmost=idx
            rightmost=idx
            if idx>0 and left[idx-1]!=-1:
                leftmost=left[idx-1]
            if idx+1<total and right[idx+1]!=-1:
                rightmost=right[idx+1]
            left[idx]=leftmost
            right[idx]=rightmost
            left[rightmost]=leftmost
            right[leftmost]=rightmost
            if rightmost-idx==m:
                cnt-=1
            if idx-leftmost==m:
                cnt-=1
            if rightmost-leftmost+1==m:
                cnt+=1
            if cnt>0:
                ret=i
        return ret