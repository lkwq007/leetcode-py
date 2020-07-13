class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        ret=0
        record=[0]*26
        word_letters=[record[:] for item in words]
        base=ord("a")
        for item in letters:
            record[ord(item)-base]+=1
        for idx in range(len(words)):
            for item in words[idx]:
                word_letters[idx][ord(item)-base]+=1
        self.max=0
        def probe(lst,count,total):
            if len(lst)<1:
                self.max=max(self.max,total)
                return
            word=lst[0]
            cnt=0
            acc=0
            for idx in range(len(word)):
                count[idx]-=word[idx]
                acc+=word[idx]*score[idx]
                if count[idx]<0:
                    cnt+=1
            if cnt==0:
                probe(lst[1:],count,total+acc)
            cnt=0
            for idx in range(len(word)):
                count[idx]+=word[idx]
                if count[idx]<0:
                    cnt+=1
            if cnt==0:
                probe(lst[1:],count,total)
        probe(word_letters,record,0)
        return self.max