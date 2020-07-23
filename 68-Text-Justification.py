class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ret=[]
        row=[]
        cnt=0
        for item in words:
            if cnt==0:
                row.append(item)
                cnt+=len(item)
            else:
                tmp=cnt+len(item)+1
                if tmp>maxWidth:
                    ret.append(row)
                    cnt=len(item)
                    row=[item]
                else:
                    row.append(item)
                    cnt=tmp
        if cnt:
            ret.append(row)
        ret[-1]=[" ".join(ret[-1])]
        for i in range(len(ret)):
            lst=ret[i]
            if len(lst)==1:
                ret[i]=lst[0]+" "*(maxWidth-len(lst[0]))
            else:
                total=0
                for word in lst:
                    total+=len(word)
                spaces=(maxWidth-total)//(len(lst)-1)
                space=" "*spaces
                extra=(maxWidth-total)%(len(lst)-1)
                line=lst[0]
                for j in range(1,len(lst)):
                    line+=space
                    if j<=extra:
                        line+=" "
                    line+=lst[j]
                ret[i]=line
        return ret