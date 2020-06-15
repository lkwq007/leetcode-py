class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        zero=ord("0")
        len1=len(num1)
        len2=len(num2)
        carry=0
        if len1<len2:
            num1,num2=num2,num1
            len1,len2=len2,len1
        ret=""
        idx=-1
        while idx>=-len2:
            val=ord(num1[idx])+ord(num2[idx])-zero-zero+carry
            if val>9:
                val-=10
                carry=1
            else:
                carry=0
            ret+=chr(val+zero)
            idx-=1
        while idx>=-len1:
            val=ord(num1[idx])-zero+carry
            if val>9:
                val-=10
                carry=1
            else:
                carry=0
            ret+=chr(val+zero)
            idx-=1
        if carry:
            ret+="1"
        return ret[::-1]