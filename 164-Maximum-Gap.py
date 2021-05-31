class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        def sort(lst,radix):
            if radix<1 or len(lst)<2:
                return lst
            cur=radix
            ret=[]
            last=0
            while cur<=10*radix:
                left=[]
                right=[]
                for item in lst:
                    if item<cur:
                        left.append(item-last)
                    else:
                        right.append(item)
                ret+=[item+last for item in sort(left,radix//10)]
                lst=right
                last=cur
                cur+=radix
            return ret
        new_nums=sort(nums,10**9)
        ret=0
        # print(new_nums)
        for i in range(1,len(new_nums)):
            ret=max(new_nums[i]-new_nums[i-1],ret)
        return ret
            


# class Solution:
#     def maximumGap(self, nums: List[int]) -> int:
#         nums.sort()
#         ret=0
#         for i in range(1,len(nums)):
#             ret=max(nums[i]-nums[i-1],ret)
#         return ret