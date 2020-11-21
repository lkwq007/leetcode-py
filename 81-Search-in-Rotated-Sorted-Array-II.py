class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums)<1:
            return False
        if len(nums)<2:
            return nums[0]==target
        def search(left,right):
            while left<right:
                middle=left+(right-left)//2
                if nums[left]==target or nums[right]==target or nums[middle]==target:
                    return True
                if nums[left]<nums[right]:
                    if nums[middle]<target:
                        left=middle+1
                    else:
                        right=middle
                elif nums[left]>nums[right]:
                    # left middle pivot right
                    if nums[left]<=nums[middle]:
                        if nums[left]<target<nums[middle]:
                            right=middle
                        else:
                            left=middle+1
                        # if nums[middle]<target:
                        #     left=middle+1
                        # elif nums[left]<target<nums[middle]:
                        #     right=middle
                        # else:
                        #     left=middle+1
                    # left pivot middle right
                    elif nums[middle]<=nums[right]:
                        if nums[middle]<target<nums[right]:
                            left=middle+1
                        else:
                            right=middle
                    else:
                        return False
                else:
                    # we entered a ambiguous region
                    # left middle pivot right
                    if nums[left]<nums[middle]:
                        if nums[left]<target<nums[middle]:
                            right=middle
                        else:
                            left=middle+1
                    elif nums[middle]<nums[right]:
                        if nums[middle]<target<nums[right]:
                            left=middle+1
                        else:
                            right=middle
                    else:
                        return search(left,middle) or search(middle+1,right)
            return nums[left]==target
        return search(0,len(nums)-1)