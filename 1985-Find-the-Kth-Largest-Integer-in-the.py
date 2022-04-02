class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        total=max(map(len,nums))
        lst=[(("0"*(total-len(item)))+item,i) for i,item in enumerate(nums)]
        lst.sort()
        return nums[lst[-k][1]]

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key=lambda x:(len(x),x))
        return nums[-k]