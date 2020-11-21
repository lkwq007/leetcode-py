class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        digits.sort()
        total=len(str(n))
        count=[0]*total
        for i in range(0,total):
            count[i]=len(digits)**i
        # iterate through num of digits
        template=str(n)
        def probe(i):
            if i==total:
                return 0
            cur=template[i]
            j=0
            ret=0
            while j<len(digits) and digits[j]<cur:
                j+=1
            if i==total-1:
                ret=j*count[total-i-1]
            else:
                ret=(j+1)*count[total-i-1]
            if j<len(digits) and digits[j]==cur:
                ret+=probe(i+1)
            else:
                for k in range(i+1,total-1):
                    ret+=count[total-k-1]
            return ret
        return probe(0)