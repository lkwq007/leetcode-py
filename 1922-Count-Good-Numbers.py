class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.
        even=(n+(n%2))//2
        odd=n//2
        term=10**9+7
        def pow(base,x):
            base=base%term
            if x==0:
                return 1
            if x&1:
                return (base*pow(base*base,x>>1))%term
            else:
                return pow(base*base,x>>1)%term
        return (pow(5,even)*pow(4,odd))%term

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.
        even=(n+(n%2))//2
        odd=n//2
        term=10**9+7
        def pow(base,x):
            ret=1
            while x>0:
                if x&1:
                    ret=(ret*base)%term
                base=(base*base)%term
                x=x>>1
        return (pow(5,even)*pow(4,odd))%term