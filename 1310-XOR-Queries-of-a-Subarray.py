class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        acc=0
        for idx in range(len(arr)):
            acc^=arr[idx]
            arr[idx]=acc
        arr.append(0)
        return list(map(lambda x: arr[x[0]-1]^arr[x[1]],queries))

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        acc=0
        for idx in range(len(arr)):
            acc^=arr[idx]
            arr[idx]=acc
        ret=list(map(lambda x: arr[x[1]]^(arr[x[0]-1] if x[0]>0 else 0),queries))
        for idx in range(len(arr)-1,0,-1):
            arr[idx]^=arr[idx-1]
        return ret