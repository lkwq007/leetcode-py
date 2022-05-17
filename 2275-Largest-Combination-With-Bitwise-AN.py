class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        record={}
        for item in candidates:
            mask=1
            while item>=mask:
                if item&mask:
                    record[mask]=record.get(mask,0)+1
                mask=mask<<1
        return max(list(record.values()))