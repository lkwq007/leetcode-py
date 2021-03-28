class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        record={}
        start=0
        while start<len(word):
            if word[start].isalpha():
                start+=1
            elif word[start].isdigit():
                end=start
                while end<len(word) and word[end].isdigit():
                    end+=1
                record[int(word[start:end])]=1
                start=end
        return len(record)