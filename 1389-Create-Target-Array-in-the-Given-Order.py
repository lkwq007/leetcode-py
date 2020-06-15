class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ret=[None]*len(nums)
        idx_list=[]
        total=0
        for i,item in enumerate(index,0):
            if i==item:
                idx_list.append(item)
            else:
                for j in range(0,len(idx_list)):
                    if idx_list[j]>=item:
                        idx_list[j]+=1
                idx_list.append(item)
        for i,idx in enumerate(idx_list,0):
            ret[idx]=nums[i]
        return ret

# class Solution:
#     def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
#         ret=[None]*len(nums)
#         idx_list=[]
#         total=0
#         for i,item in enumerate(index,0):
#             if i==item:
#                 idx_list.append(item)
#             else:
#                 for j in range(0,len(idx_list)):
#                     if idx_list[j]>=item:
#                         idx_list[j]+=1
#                 idx_list.append(item)
#         for i,idx in enumerate(idx_list,0):
#             ret[idx]=nums[i]
#         return ret