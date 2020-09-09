class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        if len(arr)<m*k:
            return False
        total=m*k
        for i in range(len(arr)-total+1):
            for offset in range(m):
                item=arr[i+offset]
                for idx in range(i,i+total,m):
                    if arr[idx+offset]!=item:
                        
        return False