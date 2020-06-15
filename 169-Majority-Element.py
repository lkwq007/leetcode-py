from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer–Moore majority vote algorithm
        counter=0
        majority=nums[0]
        for item in nums:
            if counter==0:
                majority=item
                counter=1
            elif item==majority:
                counter+=1
            else:
                counter-=1
        return majority
x=Solution()
print(x.majorityElement([3,3,4]))
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapping={}
        majority=nums[0]
        for item in nums:
            if item in mapping:
                mapping[item]+=1
            else:
                mapping[item]=1
            if mapping[item]>mapping[majority]:
                majority=item
        return majority