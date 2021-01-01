class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome)<2:
            return ""
        lst=list(palindrome)
        for i in range((len(palindrome))//2):
            if palindrome[i]!="a":
                lst[i]="a"
                return "".join(lst)
        lst[-1]="b"
        return "".join(lst)