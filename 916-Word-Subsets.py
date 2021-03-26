class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        reference=[0]*26
        base=ord("a")
        for word in B:
            lst=[0]*26
            for item in word:
                lst[ord(item)-base]+=1
            for i in range(26):
                reference[i]=max(reference[i],lst[i])
        ret=[]
        for word in A:
            lst=[0]*26
            for item in word:
                lst[ord(item)-base]+=1
            flag=True
            for i in range(26):
                if lst[i]<reference[i]:
                    flag=False
                    break
            if flag:
                ret.append(word)
        return ret