class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        record={}
        for item in arr:
            record[item]=record.get(item,0)+1
        meta={}
        for val in record.values():
            if val in meta:
                return False
            meta[val]=1
        return True