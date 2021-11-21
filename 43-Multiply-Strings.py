class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"
        def add(a,b):
            acc=""
            carry=0
            if len(a)<len(b):
                a,b=b,a
            for i in range(1,len(b)+1):
                cur=int(a[-i])+int(b[-i])+carry
                if cur>9:
                    cur-=10
                    carry=1
                else:
                    carry=0
                acc+=str(cur)
            for i in range(len(b)+1,len(a)+1):
                cur=int(a[-i])+carry
                if cur>9:
                    cur-=10
                    carry=1
                else:
                    carry=0
                acc+=str(cur)
            if carry==1:
                acc+="1"
            return acc[::-1]
        if len(num1)<len(num2):
            num1,num2=num2,num1
        ret="0"
        for i in range(1,len(num2)+1):
            carry=0
            acc=""
            val=int(num2[-i])
            for j in range(1,len(num1)+1):
                cur=int(num1[-j])
                cur=cur*val+carry
                carry=cur//10
                cur=cur%10
                acc+=str(cur)
            if carry!=0:
                acc+=str(carry)
            ret=add(ret,acc[::-1]+("0"*(i-1)))
        return ret
