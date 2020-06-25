class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        def convert(x):
            if x%3==0 and x%5==0:
                return "FizzBuzz"
            elif x%3==0:
                return "Fizz"
            elif x%5==0:
                return "Buzz"
            return str(x)
        return [convert(x) for x in range(1,n+1)]

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret=[]
        fizz=0
        buzz=0
        for i in range(1,n+1):
            fizz+=1
            buzz+=1
            if fizz==3 and buzz==5:
                ret.append("FizzBuzz")
                fizz=0
                buzz=0
            elif fizz==3:
                ret.append("Fizz")
                fizz=0
            elif buzz==5:
                ret.append("Buzz")
                buzz=0
            else:
                ret.append(str(i))
        return ret

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret=[str(i) for i in range(1,n+1)]
        mapping=[(3,"Fizz"),(5,"Buzz"),(15,"FizzBuzz")]
        for step,word in mapping:
            for i in range(step-1,n,step):
                ret[i]=word
        return ret