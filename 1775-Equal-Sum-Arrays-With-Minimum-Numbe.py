class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        min1,min2=len(nums1),len(nums2)
        max1,max2=min1*6,min2*6
        if min1>max2 or min2>max1:
            return -1
        lst1=[0]*7
        lst2=[0]*7
        total1=0
        total2=0
        for item in nums1:
            lst1[item]+=1
            total1+=item
        for item in nums2:
            lst2[item]+=1
            total2+=item
        if total1==total2:
            return 0
        elif total2>total1:
            total1,total2=total2,total1
            lst1,lst2=lst2,lst1
        diff=total1-total2
        ret=0
        for i in range(6,1,-1):
            total=lst1[i]+lst2[7-i]
            cur=i-1
            if diff>total*cur:
                diff-=total*cur
                ret+=total
            else:
                ret+=(diff+cur-1)//cur
                break
        return ret