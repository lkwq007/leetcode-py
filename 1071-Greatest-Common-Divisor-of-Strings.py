class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1=len(str1)
        len2=len(str2)
        def gcd(a,b):
            while b>0:
                a,b=b,a%b
            return a
        l=gcd(len1,len2)
        for i in range(l,0,-1):
            if len1%i==0 and len2%i==0:
                flag=True
                for j in range(0,len1,i):
                    if str1[:i]!=str1[j:j+i]:
                        flag=False
                        break
                if flag:
                    for j in range(0,len2,i):
                        if str1[:i]!=str2[j:j+i]:
                            flag=False
                            break
                if flag:
                    return str1[:i]
        return ""
