from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings)<2:
            return len(ratings)
        record={}
        for idx,item in enumerate(ratings,0):
            if item in record:
                record[item].append(idx)
            else:
                record[item]=[idx]
        keys=list(record.keys())
        keys.sort()
        total=len(ratings)
        alloc=[0]*(total+1)
        for key in keys:
            lst=record[key]
            for idx in lst:
                left=0 if idx==0 else ratings[idx-1]
                right=0 if idx==total-1 else ratings[idx+1]
                if key<=left and key<=right:
                    alloc[idx]=1
                elif key<=left:
                    alloc[idx]=alloc[idx+1]+1
                elif key<=right:
                    alloc[idx]=alloc[idx-1]+1
                else:
                    alloc[idx]=max(alloc[idx+1],alloc[idx-1])+1
        return sum(alloc)
x=Solution()
print(x.candy([1,2,2]))