
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        cnt=0
        total=(k-1)*m
        for i in range(m,len(arr)):
            if arr[i]!=arr[i-m]:
                cnt=0
            else:
                cnt+=1
            if cnt==total:
                return True
        return False

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        if m*k>len(arr):
            return False
        mk=m*k
        for i in range(len(arr)-m+1):
            idx=i
            total=0
            for j in range(m):
                idx=i+j
                cnt=0
                item=arr[idx]
                while cnt<k and idx<len(arr):
                    if arr[idx]==item:
                        cnt+=1
                        idx+=m
                    else:
                        break
                total+=cnt
                if cnt!=k:
                    break
            if total==mk:
                return True
        return False