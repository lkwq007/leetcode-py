class Solution:
    def minSwaps(self, s: str) -> int:
        ones=0
        zeros=0
        for item in s:
            if item=="0":
                zeros+=1
            else:
                ones+=1
        if abs(zeros-ones)>1:
            return -1
        zero_first=0
        one_first=0
        cur0=0
        cur1=1
        for item in s:
            if item!=str(cur0):
                zero_first+=1
            if item!=str(cur1):
                one_first+=1
            cur0=1-cur0
            cur1=1-cur1
        if zeros>ones:
            return zero_first//2
        elif ones>zeros:
            return one_first//2
        else:
            return min(one_first,zero_first)//2