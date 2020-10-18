class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        record={}
        for item in A:
            record[item]=record.get(item,0)+1
        if record.get(0,0)%2==1:
            return False
        elif 0 in record:
            del record[0]
        last=len(record)+1
        while last!=len(record):
            last=len(record)
            for key in list(record.keys()):
                if key not in record:
                    continue
                if key%2!=0:
                    if record.get(key*2,0)<record[key]:
                        return False
                    record[key*2]-=record[key]
                    if record[key*2]==0:
                        del record[key*2]
                    del record[key]
                else:
                    half=record.get(key//2,0)
                    double=record.get(key*2,0)
                    if half+double<record[key]:
                        return False
                    if half==0:
                        record[key*2]-=record[key]
                        if record[key*2]==0:
                            del record[key*2]
                        del record[key]
                    elif double==0:
                        record[key//2]-=record[key]
                        if record[key//2]==0:
                            del record[key//2]
                        del record[key]
        return len(record)==0