class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        num=str(x)
        total=len(num)
        for i in range(0,total//2):
            if num[i]!=num[total-i-1]:
                return False
        return True

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        lst=[]
        while x>0:
            tmp=x%10
            lst.append(tmp)
            x=x//10
        total=len(lst)
        for i in range(0,total//2):
            if lst[i]!=lst[total-i-1]:
                return False
        return True