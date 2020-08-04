class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if len(arr2)>len(arr1):
            arr1,arr2=arr2,arr1
        ptr1=len(arr1)-1
        ptr2=len(arr2)-1
        ret=[]
        mask=1
        carry=0
        while ptr2>=0:
            cur=arr1[ptr1]+arr2[ptr2]-carry
            if cur>1:
                carry=1
                ret.append(1)
            elif cur<0:
                carry=1
                ret.append(1)
            else:
                ret.append(cur)
                carry=0
            ptr1-=1
            ptr2-=1
        while ptr1>=0:
            cur=arr1[ptr1]-carry
            if cur>1:
                carry=1
                ret.append(1)
            elif cur<0:
                carry=1
                ret.append(1)
            else:
                ret.append(cur)
                carry=0
            ptr1-=1
        if carry:
            ret.append(1)
        return reversed(ret)