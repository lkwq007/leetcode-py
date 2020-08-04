class Solution:
    def convertToBase7(self, num: int) -> str:
        def convert(x):
            ret=[]
            while x>0:
                ret.append(str(x%7))
                x=x//7
            return "".join(reversed(ret))
        if num<0:
            return "-"+convert(-num)
        elif num==0:
            return "0"
        return convert(num)