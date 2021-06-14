class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def check(idx0,idx1):
            word=words[idx0]+words[idx1]
            for i in range(len(word)//2):
                if word[i]!=word[len(word)-i-1]:
                    return False
            return True
        record={}
        mapping={}
        mask=1
        base=ord("a")
        for i in range(26):
            mapping[chr(base+i)]=mask
            mask=mask<<1
        for i in range(len(words)):
            acc=0
            word=words[i]
            for item in word:
                acc^=mapping[item]
            # print(acc)
            if acc not in record:
                record[acc]=[]
            record[acc].append(i)
        ret=[]
        for k,v in record.items():
            if len(v)>1:
                for i in range(len(v)):
                    for j in range(i+1,len(v)):
                        if check(v[i],v[j]):
                            ret.append([v[i],v[j]])
                        if check(v[j],v[i]):
                            ret.append([v[j],v[i]])
        return ret