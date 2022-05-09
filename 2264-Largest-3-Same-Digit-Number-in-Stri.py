class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ret=""
        for i in range(2,len(num)):
            if num[i]==num[i-1]==num[i-2]:
                if len(ret)==0 or ret<num[i]:
                    ret=num[i]
        return ret*3