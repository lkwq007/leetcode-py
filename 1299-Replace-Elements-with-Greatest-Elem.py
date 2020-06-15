class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr)<1:
            return arr
        last=arr[-1]
        arr[-1]=-1
        for idx in range(len(arr)-2,-1,-1):
            tmp=last
            if arr[idx]>last:
                last=arr[idx]
            arr[idx]=tmp
        return arr
