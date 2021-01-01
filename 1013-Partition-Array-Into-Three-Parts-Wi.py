class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total=sum(arr)
        if total%3!=0:
            return False
        acc=0
        first=total//3
        second=first*2
        flag=False
        for i in range(len(arr)):
            item=arr[i]
            acc+=item
            if acc==second and flag and i<len(arr)-1:
                return True
            if acc==first:
                flag=True
        return False