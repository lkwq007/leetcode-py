class Solution:
    def minimumDeletions(self, s: str) -> int:
        a=0
        for item in s:
            if item=="a":
                a+=1
        b=len(s)-a
        ret=min(a,b)
        acc_a=0
        acc_b=0
        for i in range(len(s)):
            if s[i]=="a":
                acc_a+=1
            else:
                acc_b+=1
            ret=min(acc_b+a-acc_a,ret)
        return ret