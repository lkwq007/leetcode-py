class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        record={}
        for idx,item in enumerate(ring,0):
            if item not in record:
                record[item]=[]
            record[item].append(idx)
        