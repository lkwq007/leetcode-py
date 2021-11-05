class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        record={}
        for item in arr:
            record[item]=record.get(item,0)+1
        idx=0
        for item in arr:
            if record[item]==1:
                idx+=1
                if idx==k:
                    return item
        return ""