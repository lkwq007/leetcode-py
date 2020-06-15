class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:x[0]-x[1])
        return sum([item[0] for item in costs[:(len(costs)//2)]])+sum([item[1] for item in costs[(len(costs)//2):]])

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:-abs(x[0]-x[1]))
        acc=0
        cnt0=0
        cnt1=0
        total=len(costs)//2
        for a,b in costs:
            if a<b and cnt0<total:
                acc+=a
                cnt0+=1
            elif b<a and cnt1<total:
                acc+=b
                cnt1+=1
            elif cnt0>=total:
                acc+=b
                cnt1+=1
            else:
                acc+=a
                cnt0+=1
        return acc