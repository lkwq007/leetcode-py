class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        disjoint=[-1]*len(words)
        mapping={}
        mask=1
        for i in range(26):
            mapping[chr(ord("a")+i)]=mask
            mask=mask<<1
        def convert(word):
            acc=0
            for item in word:
                acc|=mapping[item]
            return acc
        dual={}
        mask0=1
        for i in range(26):
            mask1=1
            for j in range(26):
                dual[mask0|mask1]=1
                mask1=mask1<<1
            mask0=mask0<<1
        lst=[]
        word_lst=[[] for _ in range(27)]
        for i in range(len(words)):
            acc=convert(words[i])
            lst.append(acc)
            word_lst[len(words[i])].append(i)
        def find(x):
            next=x
            while disjoint[next]>=0:
                next=disjoint[next]
            while disjoint[x]>=0:
                tmp=disjoint[x]
                disjoint[x]=next
                x=tmp
            return next
        def union(a,b):
            ai=find(a)
            bi=find(b)
            if ai!=bi:
                disjoint[ai]+=disjoint[bi]
                disjoint[bi]=ai
        for i in range(26):
            cur_lst=word_lst[i]
            for j in range(len(cur_lst)):
                for k in range(j+1,len(cur_lst)):
                    acc0=lst[cur_lst[j]]
                    acc1=lst[cur_lst[k]]
                    if acc0==acc1 or (acc0^acc1 in dual):
                        union(cur_lst[j],cur_lst[k])
            for other_lst in [word_lst[i-1],word_lst[i+1]]:
                for i0 in cur_lst:
                    for i1 in other_lst:
                        acc0=lst[i0]
                        acc1=lst[i1]
                        mask=acc0^acc1
                        if (mask&(mask-1))==0:
                            union(i0,i1)
        cnt=0
        ret=0
        for item in disjoint:
            if item<0:
                cnt+=1
            ret=min(ret,item)
        print(disjoint)
        return [cnt,-ret]

class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        disjoint=[-1]*len(words)
        mapping={}
        mask=1
        for i in range(26):
            mapping[chr(ord("a")+i)]=mask
            mask=mask<<1
        def convert(word):
            acc=0
            for item in word:
                acc|=mapping[item]
            return acc
        dual={}
        mask0=1
        for i in range(26):
            mask1=1
            for j in range(26):
                dual[mask0|mask1]=1
                mask1=mask1<<1
            mask0=mask0<<1
        lst=[]
        word_lst=[[] for _ in range(27)]
        record={}
        for i in range(len(words)):
            acc=convert(words[i])
            lst.append(acc)
            if acc in record:
                disjoint[record[acc]]-=1
                disjoint[i]=record[acc]
            else:
                record[acc]=i
        def find(x):
            next=x
            while disjoint[next]>=0:
                next=disjoint[next]
            while disjoint[x]>=0:
                tmp=disjoint[x]
                disjoint[x]=next
                x=tmp
            return next
        def union(a,b):
            ai=find(a)
            bi=find(b)
            if ai!=bi:
                disjoint[ai]+=disjoint[bi]
                disjoint[bi]=ai
        for k,v in record.items():
            mask=1
            target=None
            for i in range(26):
                if k&mask:
                    target=k^mask
                    other=1
                    for j in range(26):
                        if other&target==0:
                            new_target=target|other
                            if new_target in record:
                                union(v,record[new_target])
                        other=other<<1
                else:
                    target=k|mask
                if target in record:
                    union(v,record[target])
                mask=mask<<1
        cnt=0
        ret=0
        for item in disjoint:
            if item<0:
                cnt+=1
            ret=min(ret,item)
        # print(disjoint)
        return [cnt,-ret]