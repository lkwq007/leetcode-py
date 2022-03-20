class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        stack=[nums[0]]
        for item in nums[1:]:
            if item==stack[-1]:
                continue
            stack.append(item)
        ret=0
        for i in range(1,len(stack)-1):
            if stack[i-1]<stack[i] and stack[i+1]<stack[i]:
                ret+=1
            if stack[i-1]>stack[i] and stack[i+1]>stack[i]:
                ret+=1
        return ret