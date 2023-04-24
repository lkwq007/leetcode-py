class Solution:
    def sumOfMultiples(self, n: int) -> int:
        acc=0
        for i in range(1,n+1):
            if i%3==0 or i%5==0 or i%7==0:
                acc+=i
        return acc

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def count(x):
            return (1+x)*x//2
        return count(n//3)*3+count(n//5)*5+count(n//7)*7-count(n//15)*15-count(n//21)*21-count(n//35)*35+count(n//105)*105