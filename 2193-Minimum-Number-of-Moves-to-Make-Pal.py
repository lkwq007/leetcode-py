class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        # greedy
        record={}
        for i in range(len(s)):
            item=s[i]
            if item not in record:
                record[item]=[]
            record[item].append(i)
        s=list(s)
        ret=0
        for i in range(len(s)//2):
            left=s[i]
            right=s[len(s)-i-1]
            if left==right:
                record[left].pop()
                record[left].pop(0)
            else:
                flag=True
                if len(record[left])<=1:
                    flag=False
                elif len(record[right])<=1:
                    pass
                else:
                    l=record[left][-1]
                    r=record[right][0]
                    if len(s)-i-1-l>r-i:
                        flag=False
                if flag:
                    idx=record[left].pop()
                    record[left].pop(0)
                    ret+=len(s)-i-1-idx
                    for k in record.keys():
                        for i in range(len(record[k])):
                            item=record[k][i]
                            if item>idx:
                                record[k][i]=item-1
                                s[item-1]=k
                else:
                    record[right].pop()
                    idx=record[right].pop(0)
                    ret+=idx-i
                    for k in record.keys():
                        for i in range(len(record[k])):
                            item=record[k][i]
                            if item<idx:
                                record[k][i]=item+1
                                s[item+1]=k
        return ret