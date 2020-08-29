# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        mapping={}
        cnt=0
        cur=1
        for y in range(1,8):
            for x in range(1,8):
                cnt+=1
                if cnt>4:
                    cnt=1
                    cur+=1
                if cur>10:
                    break
                mapping[(y,x)]=cur
        while True:
            y=rand7()
            x=rand7()
            if (y,x) in mapping:
                return mapping[(y,x)]

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        step=(7**3)//10
        while True:
            x=rand7()
            y=rand7()
            z=rand7()
            idx=(z-1)*49+(y-1)*7+x-1
            cur=idx//step+1
            if cur<11:
                return cur
