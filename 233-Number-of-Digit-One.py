class Solution:
    def countDigitOne(self, n: int) -> int:
        def ones(digits):
            return digits*(10**(digits-1))
        def count(x):
            if x<10:
                return 1 if x>=1 else 0
            tmp=str(x)
            total=len(tmp)-1
            if tmp[0]=="1":
                rest=int(tmp[1:])
                return rest+count(rest)+count(int("9"*total))
            else:
                first=int(tmp[0])
                rest=int(tmp[1:])
                return count(rest)+(first-1)*ones(total)+(10**total)+count(int("9"*total))
        return count(n)