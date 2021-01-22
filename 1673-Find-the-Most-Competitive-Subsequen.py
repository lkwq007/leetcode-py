class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack=[]
        idx=0
        while idx<len(nums):
            while stack and nums[idx]<stack[-1] and len(nums)-idx>=k-len(stack)+1:
                stack.pop()
            stack.append(nums[idx])
            idx+=1
        return stack[:k]



# class Solution:
#     def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
#         # dirty sol
#         if k<2:
#             return [min(nums)]
#         total=len(nums)
#         lst=[]
#         def probe(pos,rest):
#             if rest==1:
#                 lst.append(min(nums[pos:]))
#                 return True
#             min_idx=pos
#             for i in range(pos,total-rest+1):
#                 if nums[i]<nums[min_idx]:
#                     min_idx=i
#                 if nums[i]==0 or total==10**5:
#                     break
#             lst.append(nums[min_idx])
#             for i in range(pos,total-rest+1):
#                 if nums[i]==nums[min_idx]:
#                     if probe(i+1,rest-1):
#                         return True
#             lst.pop()
#             return False
#         probe(0,k)
#         return lst