class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        lst_a=list(A)
        lst_b=list(B)
        for i in range(len(A)):
            if lst_a[i]==lst_b[i]:
                lst_a[i]=""
                lst_b[i]=""
        A="".join(lst_a)
        B="".join(lst_b)
        if len(A)<=2:
            return len(A)//2
        queue=[(A,B)]
        record={}
        step=0
        while queue:
            target=[]
            step+=1
            for a,b in queue:
                a0=a[0]
                b0=b[0]
                a_template=list(a[1:])
                b_template=b[1:]
                for i in range(len(a_template)):
                    if a_template[i]==b0:
                        a_template[i]=a0
                        a_next="".join(a_template)
                        b_next=b_template
                        j=0
                        while j<len(a_next) and a_next[j]==b_next[j]:
                            j+=1
                        a_next=a_next[j:]
                        b_next=b_next[j:]
                        if a_next==b_next:
                            return step
                        if (a_next,b_next) not in record:
                            record[(a_next,b_next)]=step
                            target.append((a_next,b_next))
                        a_template[i]=b0
            queue=target
        return step