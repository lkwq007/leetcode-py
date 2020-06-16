class Solution:
    def maxScore(self, s: str) -> int:
        # one pass
        zeros=1 if s[0]=="0" else 0
        ones=1-zeros
        max_val=zeros-ones
        for item in s[1:-1]:
            if item=="1":
                ones+=1
            else:
                zeros+=1
            max_val=max(max_val,zeros-ones)
        tmp=1 if s[-1]=="1" else 0
        return max_val+ones+tmp
            
            
class Solution:
    def maxScore(self, s: str) -> int:
        ones=0
        for item in s[1:]:
            if item=="1":
                ones+=1
        zeros=1 if s[0]=="0" else 0
        max_val=ones+zeros
        for item in s[1:-1]:
            if item=="1":
                ones-=1
            else:
                zeros+=1
            max_val=max(max_val,ones+zeros)
        return max_val