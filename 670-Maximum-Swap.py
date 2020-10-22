class Solution:
    def maximumSwap(self, num: int) -> int:
        def swap(idx,lst):
            if idx==len(lst)-1:
                return
            max_idx=idx
            for i in range(idx,len(lst)):
                if lst[max_idx]<=lst[i]:
                    max_idx=i
            if max_idx!=idx and lst[idx]<lst[max_idx]:
                lst[max_idx],lst[idx]=lst[idx],lst[max_idx]
            else:
                swap(idx+1,lst)
        lst=list(str(num))
        swap(0,lst)
        return int("".join(lst))