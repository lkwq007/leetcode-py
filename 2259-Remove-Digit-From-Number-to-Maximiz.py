class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        lst=[]
        for i in range(len(number)):
            if number[i]==digit:
                lst.append(number[:i]+number[i+1:])
        lst.sort()
        return lst[-1]