class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        if len(a)<2:
            return True
        middle=(len(a)-1)//2
        left=middle
        right=len(a)-left-1
        while left>=0 and a[left]==a[len(a)-1-left]:
            left-=1
        pivot=left
        if pivot<0:
            return True
        flag=True
        for i in range(0,pivot+1):
            if a[i]!=b[len(a)-1-i]:
                flag=False
                break
        if flag:
            return True
        flag=True
        for i in range(0,pivot+1):
            if b[i]!=a[len(a)-1-i]:
                flag=False
                break
        if flag:
            return True
        left=middle
        while left>=0 and b[left]==b[len(a)-1-left]:
            left-=1
        pivot=left
        if pivot<0:
            return True
        flag=True
        for i in range(0,pivot+1):
            if b[i]!=a[len(a)-1-i]:
                flag=False
                break
        if flag:
            return True
        flag=True
        for i in range(0,pivot+1):
            if a[i]!=b[len(a)-1-i]:
                flag=False
                break
        if flag:
            return True
        return False