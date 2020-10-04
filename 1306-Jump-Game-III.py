class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start]==0:
            return True
        queue=[start]
        arr[start]=-arr[start]
        while queue:
            target=[]
            for i in queue:
                offset=abs(arr[i])
                idx=(i+offset,i-offset)
                for j in idx:
                    if j<0 or j>=len(arr):
                        continue
                    if arr[j]==0:
                        return True
                    if arr[j]>0:
                        target.append(j)
                        arr[j]=-arr[j]
            queue=target
        return False