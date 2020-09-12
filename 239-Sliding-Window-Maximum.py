from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue=deque([])
        for i in range(k):
            while queue and queue[-1]<nums[i]:
                queue.pop()
            queue.append(nums[i])
        ret=[queue[0]]
        for i in range(k,len(nums)):
            item=nums[i]
            left=nums[i-k]
            if left==queue[0]:
                queue.popleft()
            while queue and queue[-1]<item:
                queue.pop()
            queue.append(item)
            ret.append(queue[0])
        return ret