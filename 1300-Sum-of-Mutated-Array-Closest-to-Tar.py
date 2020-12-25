class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        acc=0
        arr.sort()
        diff=target
        ret=arr[0]
        for i in range(len(arr)):
            total=acc+(len(arr)-i)*arr[i]
            acc+=arr[i]
            cur_diff=abs(total-target)
            if cur_diff<diff:
                diff=cur_diff
                ret=arr[i]
        return ret