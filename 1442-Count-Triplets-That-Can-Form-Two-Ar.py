from typing import List
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        if len(arr)<1:
            return 0
        # xor=[0]*(len(arr)+1)
        acc=0
        record={0:[-1]}
        cnt=0
        for idx in range(0,len(arr)):
            acc=acc^arr[idx]
            if acc in record:
                for item in record[acc]:
                    cnt+=idx-item-1
                record[acc].append(idx)
            else:
                record[acc]=[idx]
            # xor[idx+1]=acc
        return cnt
x=Solution()
print(x.countTriplets([1,1,1,1,1]))