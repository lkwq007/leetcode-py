class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        # s and words[i] consist of only lowercase English letters.
        graph=[]
        record=[-1]*26
        base=ord("a")
        for i in range(len(S)-1,-1,-1):
            item=ord(S[i])-base
            graph.append(record[:])
            record[item]=i+1
        graph.append(record[:])
        graph=graph[::-1]
        ret=0
        for word in words:
            idx=0
            flag=True
            head=ord(word[0])-base
            if graph[0][head]==-1:
                continue
            idx=graph[0][head]
            for c in word[1:]:
                item=ord(c)-base
                if graph[idx][item]==-1:
                    flag=False
                    break
                idx=graph[idx][item]
            if flag:
                ret+=1
        return ret

class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        # brute force, TLE
        ret=0
        for word in words:
            i=0
            j=0
            while i<len(S) and j<len(word):
                if S[i]==word[j]:
                    i+=1
                    j+=1
                else:
                    i+=1
            if j==len(word):
                ret+=1
        return ret