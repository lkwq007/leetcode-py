class Solution:
    def intToRoman(self, num: int) -> str:
        mapping={1:"I",4:"IV",5:"V",9:"IX",10:"X",
        40:"XL",50:"L",90:"XC",100:"C",
        400:"CD",500:"D",900:"CM",1000:"M"}
        nums=list(mapping.keys())
        nums.sort(reverse=True)
        ret=""
        idx=0
        total=len(nums)
        while num>0 and idx<total:
            tmp=nums[idx]
            if tmp<=num:
                num-=tmp
                ret+=mapping[tmp]
            else:
                idx+=1
        return ret

x=Solution()
print(x.intToRoman(1994))
print(x.intToRoman(2944))
print(x.intToRoman(58))    