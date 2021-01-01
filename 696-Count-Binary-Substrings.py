class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        zeros=1 if s[0]=="0" else 0
        ones=1-zeros
        last=s[0]
        ret=0
        for item in s[1:]:
            if item=="0":
                if item==last:
                    zeros+=1
                else:
                    zeros=1
                if zeros<=ones:
                    ret+=1
            else:
                if item==last:
                    ones+=1
                else:
                    ones=1
                if ones<=zeros:
                    ret+=1
            last=item
        return ret