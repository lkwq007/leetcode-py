class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        single={}
        double={}
        for item in arr:
            if item in double or item*2 in single:
                return True
            double[item*2]=1
            single[item]=1
        return False

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        record=set()
        for item in arr:
            if item*2 in record or (item%2==0 and item//2 in record):
                return True
            record.add(item)
        return False