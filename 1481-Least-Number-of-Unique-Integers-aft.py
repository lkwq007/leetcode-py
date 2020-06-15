class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        if k>=len(arr)-1:
            return len(arr)-k
        record={}
        for item in arr:
            record[item]=record.get(item,0)+1
        keys=list(record.keys())
        keys.sort(key=lambda x:record[x])
        total=len(keys)
        for key in keys:
            k-=record[key]
            if k==0:
                return total-1
            elif k<0:
                return total
            else:
                total-=1
        return total