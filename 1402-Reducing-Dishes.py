class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        if satisfaction[0]<=0:
            return 0
        acc=0
        total=0
        for item in satisfaction:
            if total+item<0:
                break
            total+=item
            acc+=total
        return acc
    
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        if satisfaction[0]<=0:
            return 0
        max_val=0
        acc=0
        total=0
        for item in satisfaction:
            acc,total=item+acc+total,total+item
            max_val=max(acc,max_val)
        return max_val