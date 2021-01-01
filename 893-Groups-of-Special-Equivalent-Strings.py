class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        # brute force
        record={}
        for word in A:
            first=[word[i] for i in range(len(word))]
            second=[word[i] for i in range(1,len(word),2)]
            first.sort()
            second.sort()
            item="".join(first+second)
            record[item]=1
        return len(record)