class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def check(x):
            tmp=x
            while x>0:
                digit=x%10
                if digit==0 or tmp%digit:
                    return False
                x=x//10
            return True
        ret=[]
        for idx in range(left,right+1):
            if check(idx):
                ret.append(idx)
        return ret
