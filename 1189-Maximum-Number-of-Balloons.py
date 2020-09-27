class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        record={}
        for item in text:
            record[item]=record.get(item,0)+1
        return min([record.get(item,0) for item in "ban"]+[record.get(item,0)//2 for item in "lo"])