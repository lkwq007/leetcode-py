class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        lst=[0]*len(nums)
        for i in range(len(nums)):
            item=nums[i]
            lst[i]=(threshold+item)//item
        left=[0]*len(nums)
        right=left[:]
        stack=[]
        for i in range(len(lst)):
            while stack and lst[stack[-1]]<=lst[i]:
                stack.pop()
            left[i]=stack[-1] if stack else -1
            stack.append(i)
        stack=[]
        for i in range(len(lst)-1,-1,-1):
            while stack and lst[stack[-1]]<=lst[i]:
                stack.pop()
            right[i]=stack[-1] if stack else len(lst)
            stack.append(i)
        for i in range(len(lst)):
            # print(right[i]-left[i]-1,left[i],right[i],lst[i])
            if right[i]-left[i]-1>=lst[i]:
                return lst[i]
        return -1