class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        def factor(x):
            i=2
            ret=[1]
            while i*i<=x:
                if x%i==0:
                    ret.append(i)
                    x=x//i
                else:
                    i+=1
            if x>1:
                ret.append(x)
            return ret
        p_factor=factor(p)
        q_factor=factor(q)
        p_record={}
        q_record={}
        for a in p_factor:
            p_record[a]=p_record.get(a,0)+1
        for a in q_factor:
            q_record[a]=q_record.get(a,0)+1
        for key in q_record.keys():
            p_record[key]=max(p_record.get(key,0),q_record[key])
        tmp=1
        for key,val in p_record.items():
            tmp*=key**val
        k=tmp//q
        m=tmp//p
        if k&1 and m&1:
            return 1
        elif k&1:
            return 0
        else:
            return 2
        
