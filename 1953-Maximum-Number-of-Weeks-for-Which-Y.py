class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        ret=0
        record={}
        for item in milestones:
            record[-item]=record.get(-item,0)+1
        lst=[item for item in record.keys()]
        lst.sort()
        for i in range(len(lst)):
            