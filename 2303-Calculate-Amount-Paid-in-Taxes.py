class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        pos=0
        last=0
        ret=0
        while income>0:
            if brackets[pos][0]-last<=income:
                cur=brackets[pos][0]-last
            else:
                cur=income
            ret+=cur*float(brackets[pos][1])/100.0
            last=brackets[pos][0]
            pos+=1
            income-=cur
        return ret

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        import functools
        return functools.reduce(
            lambda acc,bracket:(acc[0]+min(acc[2],bracket[0]-acc[1])*bracket[1],bracket[0],acc[2]-min(acc[2],bracket[0]-acc[1])),brackets,(0,0,income)
        )[0]/100.0