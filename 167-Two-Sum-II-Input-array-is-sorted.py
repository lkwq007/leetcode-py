class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        while True:
            cur=numbers[left]+numbers[right]
            if cur==target:
                return [left+1,right+1]
            elif cur<target:
                left+=1
            else:
                right-=1

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        record=dict()
        for idx,item in enumerate(numbers,0):
            if (target-item) in record:
                return [record[target-item]+1,idx+1]
            record[item]=idx
            