class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        record={}
        ret=names[:]
        for i,name in enumerate(names,0):
            if name in record:
                idx=record[name]
                while f"{name}({idx})" in record:
                    idx+=1
                ret[i]=f"{name}({idx})"
                record[name]=idx+1
            else:
                ret[i]=name
            record[ret[i]]=1
        return ret