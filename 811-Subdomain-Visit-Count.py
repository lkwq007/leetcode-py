class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        record={}
        ret=[]
        for item in cpdomains:
            lst=item.split(" ")
            cnt=int(lst[0])
            domain=lst[1]
            record[domain]=record.get(domain,0)+cnt
            total=len(domain)
            idx=0
            while idx<total:
                if domain[idx]==".":
                    tmp=domain[(idx+1):]
                    record[tmp]=record.get(tmp,0)+cnt
                idx+=1
        for key,val in record.items():
            ret.append(str(val)+" "+key)
        return ret