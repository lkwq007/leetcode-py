class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:(-x[1],x[0]))
        ret=0
        for num,unit in boxTypes:
            if truckSize>num:
                ret+=num*unit
                truckSize-=num
            else:
                ret+=truckSize*unit
                break
        return ret