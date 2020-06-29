class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        total=sum(arr)
        if total%k!=0:
            return False
        record={}
        for item in arr:
            tmp=item%k
            record[tmp]=record.get(tmp,0)+1
        for i in range(1,k//2+1):
            a=record.get(i,0)
            b=record.get(k-i,0)
            if a!=b:
                return False
        return record.get(0,0)%2==0
        