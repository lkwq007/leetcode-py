class Solution:
    def isHappy(self, n: int) -> bool:
        record=dict()
        current=n
        def square_of_digits(num):
            digits=map(lambda x: int(x),list(str(num)))
            sum=0
            for item in digits:
                sum+=item*item
            return sum
        while current!=1:
            record[current]=0
            result=square_of_digits(current)
            if result in record:
                return False
            current=result
        return True