import random
class Solution:

    def __init__(self, nums: List[int]):
        self.buffer=nums
        self.pool=nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.buffer
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        idx=random.randrange(1,len(self.pool))
        self.pool[0],self.pool[idx]=self.pool[idx],self.pool[0]
        return self.pool


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

import random
class Solution:

    def __init__(self, nums: List[int]):
        self.buffer=nums
        self.pool=nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.buffer
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        total=len(self.pool)
        i=total-1
        while i>0:
            idx=random.randrange(0,i+1)
            self.pool[i],self.pool[idx]=self.pool[idx],self.pool[i]
            i-=1
        return self.pool