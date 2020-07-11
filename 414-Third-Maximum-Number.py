class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        # simply insert
        lst=[]
        def insert(x):
            for idx in range(len(lst)):
                if x==lst[idx]:
                    return
                if x>lst[idx]:
                    lst[idx],x=x,lst[idx]
            if len(lst)<3:
                lst.append(x)
        for item in nums:
            insert(item)
        if len(lst)<3:
            return lst[0]
        return lst[-1]