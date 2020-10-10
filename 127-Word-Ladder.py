class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        record={}
        flag=False
        for word in wordList:
            record[word]=1
        if endWord not in record:
            return 0
        queue=[beginWord]
        if beginWord in record:
            del record[beginWord]
        step=1
        def cmp(a,b):
            cnt=0
            for x,y in zip(a,b):
                if x!=y:
                    cnt+=1
            return cnt==1
        while queue:
            target=[]
            step+=1
            for word in queue:
                for key in record.keys():
                    if record[key]==1 and cmp(key,word):
                        if key==endWord:
                            return step
                        target.append(key)
                        record[key]=0
            record={k:v for k,v in record.items() if v==1}
            queue=target
        return 0