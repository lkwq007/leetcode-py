class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        fmap={}
        rmap={}
        for word in wordList:
            for i in range(len(word)):
                cur=word[:i]+"*"+word[i+1:]
                if cur not in fmap:
                    fmap[cur]=[]
                fmap[cur].append(word)
        flag=False
        record={beginWord:1}
        queue=[beginWord]
        rmap[endWord]=[]
        step=0
        while queue and not flag:
            target=[]
            for item in queue:
                for i in range(len(item)):
                    cur=item[:i]+"*"+item[i+1:]
                    for next in fmap.get(cur,[]):
                        if next==item:
                            continue
                        if next==endWord:
                            flag=True
                            rmap[endWord].append(item)
                        elif next not in record and not flag:
                            record[next]=step
                            target.append(next)
                        if next in record and record[next]>=step:
                            if next not in rmap:
                                rmap[next]=[]
                            rmap[next].append(item)
            queue=target
            step+=1
        self.ret=[]
        def dfs(x,lst):
            lst.append(x)
            if x==beginWord:
                self.ret.append(lst[::-1])
                lst.pop()
                return
            for next in rmap[x]:
                dfs(next,lst)
            lst.pop()
        dfs(endWord,[])
        # print(rmap)
        return self.ret