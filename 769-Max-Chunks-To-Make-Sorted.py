class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ret=0
        idx=0
        while idx<len(arr):
            val=arr[idx]
            idx+=1
            while idx<=val and idx<len(arr):
                val=max(val,arr[idx])
                idx+=1
            ret+=1
        return ret