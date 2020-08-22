class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        stack=[nums[0]]
        for item in nums[1:]:
            if item<stack[-1]:
                if len(stack)>1:
                    return True
                stack[-1]=item
            elif item>stack[-1]:
                if len(stack)>1:
                    stack[-1]=item
                else:
                    stack.append(item)
        return False
