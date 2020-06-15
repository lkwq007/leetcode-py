class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        if len(arr)<1 or len(arr[0])<2:
            return 0
        h=len(arr)
        w=len(arr[0])
        def init(row):
            if arr[row][0]<arr[row][1]:
                return [0,1]
            else:
                return [1,0]
        def update(row,idx,cur):
            if cur<2:
                return
            if arr[row][cur]<arr[row][idx[0]]:
                idx[1]=idx[0]
                idx[0]=cur
            elif arr[row][cur]<arr[row][idx[1]]:
                idx[1]=cur
        min_idx=init(0)
        for x in range(2,w):
            update(0,min_idx,x)
        for y in range(1,h):
            last_min_idx=min_idx
            min_idx=init(y)
            for x in range(0,w):
                if x==last_min_idx[0]:
                    arr[y][x]+=arr[y-1][last_min_idx[1]]
                else:
                    arr[y][x]+=arr[y-1][last_min_idx[0]]
                update(y,min_idx,x)
        return min(arr[h-1])                    