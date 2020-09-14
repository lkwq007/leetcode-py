class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(1,len(arr)-1):
            if arr[i-1]<arr[i] and arr[i]>arr[i+1]:
                return i

# class Solution:
#     def peakIndexInMountainArray(self, arr: List[int]) -> int:
#         left=0
#         right=len(arr)
#         def check(l,r):
#             mid=l+(r-l)//2
#             if arr[l]<=arr[mid]<=arr[r] or arr[l]>=arr[mid]>=arr[r]:
#                 return False
#             return True
#         while left<right:
#             middle=left+(right-left)//2
#             if arr[middle-1]<arr[middle] and arr[middle]>arr[middle+1]:
#                 return middle
#             if check(left,middle):
#                 right=middle
#             else:
#                 left=middle+1