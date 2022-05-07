class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        min_lst=nums[:]
        for i in range(1,len(nums)):
            min_lst[i]=min(nums[i],min_lst[i-1])
        stack=[(nums[0],0)]
        for i in range(1,len(nums)):
            item=nums[i]
            left=0
            right=len(stack)-1
            while left<right:
                middle=left+(right-left)//2
                if stack[middle][0]>item:
                    left=middle+1
                else:
                    right=middle
            while left>=0 and stack[left][0]<=item:
                left-=1
            if left>=0 and min_lst[stack[left][1]]<item:
                return True
            while stack and item>=stack[-1][0]:
                stack.pop()
            stack.append((item,i))
        return False      

# from typing import List
# class Solution:
#     def find132pattern(self, nums: List[int]) -> bool:
#         # TLE
#         if len(nums)<3:
#             return False
#         lst=[]
#         stack=[nums[0]]
#         for item in nums[1:]:
#             for a,b in lst:
#                 if a<item<b:
#                     return True
#             if item<stack[-1]:
#                 if len(stack)>1 and item>stack[-2]:
#                     return True
#                 if len(stack)==1:
#                     stack[-1]=item
#                 elif len(stack)>1 and item<stack[-2]:
#                     lst.append(stack[:])
#                     stack=[item]
#             elif item>stack[-1]:
#                 if len(stack)>1:
#                     stack[-1]=item
#                     while lst and stack[-2]<=lst[-1][0] and stack[-1]>=lst[-1][1]:
#                         lst.pop()
#                 else:
#                     stack.append(item)
#         return False

# x=Solution()
# x.find132pattern([3,5,0,3,4])

# class Solution:
#     def find132pattern(self, nums: List[int]) -> bool:
#         # brute force
#         if len(nums)<3:
#             return False
#         for i in range(len(nums)):
#             j=i+1
#             while j<len(nums):
#                 while j<len(nums) and nums[j]<=nums[i]:
#                     j+=1
#                 for k in range(j+1,len(nums)):
#                     if nums[i]<nums[k]<nums[j]:
#                         return True
#         return False

        
