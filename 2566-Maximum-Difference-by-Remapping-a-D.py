class Solution:
    def minMaxDifference(self, num: int) -> int:
        max_val=0
        s=str(num)
        min_val=s.replace(s[0],"0")
        for item in s:
            if item<"9":
                break
        max_val=s.replace(item,"9")
        return int(max_val)-int(min_val)
