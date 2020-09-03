class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        total=len(s)
        head=s[0]
        for idx in range(1,(len(s)+1)//2+1):
            if total%idx==0 and s[:idx]==s[idx:idx+idx]:
                flag=True
                for i in range(idx+idx,len(s),idx):
                    if s[:idx]!=s[i:i+idx]:
                        flag=False
                        break
                if flag:
                    return True
        return False