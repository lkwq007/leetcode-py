class Solution:
    def romanToInt(self, s: str) -> int:
        mapping={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total=len(s)
        idx=0
        acc=0
        while idx<total:
            if idx!=total-1 and mapping[s[idx]]<mapping[s[idx+1]]:
                acc-=mapping[s[idx]]
            else:
                acc+=mapping[s[idx]]
            idx+=1
        return acc
x=Solution()
print(x.romanToInt("MCMXCIV"))