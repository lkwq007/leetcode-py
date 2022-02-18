class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k<1:
            return num
        if k==len(num):
            return "0"
        cnt=0
        stack=[]
        for item in num:
            tmp=int(item)
            if stack:
                while stack and stack[-1]>tmp and cnt<k:
                    stack.pop()
                    cnt+=1
                else:
                    stack.append(tmp)
            elif not stack:
                stack.append(tmp)
        acc=0
        total=len(num)-k
        return str(int("".join(map(str,stack[:total]))))
        # for item in stack:
        #     acc=acc*10+item
        # return str(acc)[:total]
x=Solution()
x.removeKdigits("1432219",3)
x.removeKdigits("10200",1)
x.removeKdigits("29200",1)
print(x.removeKdigits("1234567890",9))
print(x.removeKdigits("113",1))
print(x.removeKdigits("10001",4))