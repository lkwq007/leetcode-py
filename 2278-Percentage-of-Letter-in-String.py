class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        cnt=0
        for item in s:
            if letter==item:
                cnt+=1
        return cnt*100//len(s)