class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        length=len(words[0])
        if length*len(words)>len(s):
            return []
        # brute force
        record={}
        for word in words:
            record[word]=record.get(word,0)+1
        lst=[False]*len(s)
        for i in range(length,len(s)+1):
            word=s[i-length:i]
            if word in record:
                lst[i-length]=True
        ret=[]
        for start in range(length):
            last=start
            acc=0
            cnt={}
            for i in range(start,len(s),length):
                if not lst[i]:
                    cnt={}
                    last=i
                    acc=0
                else:
                    word=s[i:i+length]
                    acc+=1
                    cnt[word]=cnt.get(word,0)+1
                    while last<len(s) and (acc>len(words) or cnt[word]>record[word] or lst[last]==False):
                        if lst[last]:
                            acc-=1
                            cnt[s[last:last+length]]-=1
                        last+=length
                    if acc==len(words):
                        ret.append(last)
        return ret
                

