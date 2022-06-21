class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        lst=[]
        for name,time in zip(keyName,keyTime):
            h,m=map(int,time.split(":"))
            lst.append((h*60+m,name))
        lst.sort()
        last=0
        record={}
        record[lst[0][1]]=1
        ret=set([])
        for i in range(1,len(lst)):
            cur,name=lst[i]
            while last<len(lst) and lst[last][0]+60<cur:
                record[lst[last][1]]-=1
                last+=1
            if record.get(name,0)>=2:
                ret.add(name)
            record[name]=record.get(name,0)+1
        return sorted(ret)

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        record={}
        for name,time in zip(keyName,keyTime):
            h,m=map(int,time.split(":"))
            if name not in record:
                record[name]=[]
            record[name].append(h*60+m)
        ret=[]
        for k,v in record.items():
            v.sort()
            for i in range(2,len(v)):
                if v[i]-v[i-2]<=60:
                    ret.append(k)
                    break
        return sorted(ret)
