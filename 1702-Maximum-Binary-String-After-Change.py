class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        lst=list(binary)
        zero=0
        for i in range(len(binary)-1):
            if lst[i]=="0" and lst[i+1]=="0":
                lst[i]="1"
            elif lst[i]=="1" and lst[i+1]=="0":
                pos=i
                while pos>0 and lst[i]
        return "".join(lst)