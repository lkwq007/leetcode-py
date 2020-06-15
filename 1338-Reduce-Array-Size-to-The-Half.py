class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        record={}
        for item in arr:
            record[item]=record.get(item,0)+1
        keys=list(record.keys())
        keys.sort(key=lambda x:-record[x])
        total=len(arr)
        half=total//2
        cnt=0
        while total>half:
            total-=record[keys[cnt]]
            cnt+=1
        return cnt

