class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # len 1-16
        lst=[[] for _ in range(17)]
        for word in words:
            lst[len(word)].append(word)
        record={}
        ret=1
        def check(a,b):
            for i in range(len(b)):
                # print(a,b[:i]+b[i+1:])
                if a==b[:i]+b[i+1:]:
                    return True
            return False
        for i in range(16):
            for word in lst[i]:
                for next in lst[i+1]:
                    if check(word,next):
                        record[next]=max(record.get(next,1),record.get(word,1)+1)
                        ret=max(record[next],ret)
        # print(record)
        return ret