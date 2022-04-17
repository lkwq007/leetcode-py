class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        lst=list(binary)
        last=[]
        for i in range(len(binary)-1):
            if lst[i]=="1" and lst[i+1]=="0":
                if last:
                    tmp=last.pop()
                    lst[tmp]="1"
                    lst[tmp+1]="0"
                    lst[i]="0"
                    lst[i+1]="1"
                    last.append(i)
            elif lst[i]=="0" and lst[i+1]=="0":
                last.append(i+1)
                lst[i]="1"
            elif lst[i]=="0" and last==-1:
                last.append(i)
        return "".join(lst)