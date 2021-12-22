class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for item in words:
            flag=True
            for i in range(len(item)//2):
                if item[i]!=item[len(item)-1-i]:
                    flag=False
                    break
            if flag:
                return item
        return ""