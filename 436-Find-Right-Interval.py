class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # TLE
        lst=[i for i in range(len(intervals))]
        lst.sort(key=lambda x:intervals[x])
        ret=[-1]*len(intervals)
        for i in range(0,len(lst)):
            left_idx=lst[i]
            for j in range(i+1,len(lst)):
                right_idx=lst[j]
                if intervals[left_idx][1]<=intervals[right_idx][0]:
                    ret[left_idx]=right_idx
                    break
        return ret

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        lst=[i for i in range(len(intervals))]
        lst.sort(key=lambda x:intervals[x])
        ret=[-1]*len(intervals)
        for i in range(0,len(lst)-1):
            val=intervals[lst[i]][1]
            left=i+1
            right=len(intervals)
            while left<right:
                middle=left+(right-left)//2
                idx=lst[middle]
                if intervals[idx][0]>=val:
                    right=middle
                else:
                    left=middle+1
            if left<len(intervals):
                ret[lst[i]]=lst[left]
        return ret