import random
class Solution:

    def __init__(self, nums: List[int]):
        self.record={}
        for i,item in enumerate(nums):
            if item not in self.record:
                self.record[item]=[]
            self.record[item].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.record[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)