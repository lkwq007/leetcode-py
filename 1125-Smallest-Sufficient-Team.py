from typing import List
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        mask=1
        skill_mask={}
        for item in req_skills:
            skill_mask[item]=mask
            mask=mask<<1
        total_set=mask-1
        def convert(lst):
            ret=0
            for item in lst:
                ret|=skill_mask[item]
            return ret
        people_bits=[0]*len(people)
        record={}
        for idx in range(len(people)):
            mask=convert(people[idx])
            if mask==total_set:
                return [idx]
            people_bits[idx]=mask
            if mask>0:
                record[mask]=set([idx])
        while total_set not in record:
            keys=list(record.keys())
            for i in range(len(keys)):
                for j in range(i+1,len(keys)):
                    set_a=keys[i]
                    set_b=keys[j]
                    if set_a|set_b==set_b and len(record[set_a])>=len(record[set_b]):
                        del record[set_a]
                        break
                    elif set_a|set_b==set_a and len(record[set_a])<=len(record[set_b]):
                        del record[set_b]
                        keys[j]=set_a
                        break
            keys=list(record.keys())
            for i in range(len(keys)):
                for j in range(i+1,len(keys)):
                    set_a=keys[i]
                    set_b=keys[j]
                    if set_a|set_b==set_a or set_a|set_b==set_b:
                        continue
                    union=set_a|set_b
                    if union not in record:
                        record[union]=record[set_a]|record[set_b]
                    else:
                        tmp=record[set_a]|record[set_b]
                        if len(tmp)<len(record[union]):
                            record[union]=tmp
        return list(record[total_set])

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        mask=1
        skill_mask={}
        for item in req_skills:
            skill_mask[item]=mask
            mask=mask<<1
        total_set=mask-1
        def convert(lst):
            ret=0
            for item in lst:
                ret|=skill_mask[item]
            return ret
        people_bits=[0]*len(people)
        record={}
        for idx in range(len(people)):
            mask=convert(people[idx])
            if mask==total_set:
                return [idx]
            people_bits[idx]=mask
            if mask>0:
                record[mask]=set([idx])
        while total_set not in record:
            keys=list(record.keys())
            for i in range(len(keys)):
                for j in range(i+1,len(keys)):
                    set_a=keys[i]
                    set_b=keys[j]
                    if set_a|set_b==set_b and len(record[set_a])>=len(record[set_b]):
                        del record[set_a]
                        break
                    elif set_a|set_b==set_a and len(record[set_a])<=len(record[set_b]):
                        del record[set_b]
                        keys[j]=set_a
                        break
            keys=list(record.keys())
            distinct=[]
            for i in range(len(keys)):
                cnt=0
                for j in range(len(keys)):
                    if i!=j and keys[i]&keys[j]:
                        cnt+=1
                if cnt==0:
                    distinct.append(keys[i])
            if len(distinct)>1:
                acc=0
                acc_lst=set([])
                for item in distinct:
                    acc_lst=acc_lst|record[item]
                    acc|=item
                    del record[item]
                record[acc]=acc_lst
                continue
            keys=list(record.keys())
            for i in range(len(keys)):
                set_a=keys[i]
                for j in range(i+1,len(keys)):
                    set_b=keys[j]
                    if set_a|set_b==set_a or set_a|set_b==set_b:
                        continue
                    union=set_a|set_b
                    if union not in record:
                        record[union]=record[set_a]|record[set_b]
                    else:
                        tmp=record[set_a]|record[set_b]
                        if len(tmp)<len(record[union]):
                            record[union]=tmp
                del record[set_a]
        return list(record[total_set])
        

req_skills=["hfkbcrslcdjq","jmhobexvmmlyyzk","fjubadocdwaygs","peaqbonzgl","brgjopmm","x","mf","pcfpppaxsxtpixd","ccwfthnjt","xtadkauiqwravo","zezdb","a","rahimgtlopffbwdg","ulqocaijhezwfr","zshbwqdhx","hyxnrujrqykzhizm"]
people=[["peaqbonzgl","xtadkauiqwravo"],["peaqbonzgl","pcfpppaxsxtpixd","zshbwqdhx"],["x","a"],["a"],["jmhobexvmmlyyzk","fjubadocdwaygs","xtadkauiqwravo","zshbwqdhx"],["fjubadocdwaygs","x","zshbwqdhx"],["x","xtadkauiqwravo"],["x","hyxnrujrqykzhizm"],["peaqbonzgl","x","pcfpppaxsxtpixd","a"],["peaqbonzgl","pcfpppaxsxtpixd"],["a"],["hyxnrujrqykzhizm"],["jmhobexvmmlyyzk"],["hfkbcrslcdjq","xtadkauiqwravo","a","zshbwqdhx"],["peaqbonzgl","mf","a","rahimgtlopffbwdg","zshbwqdhx"],["xtadkauiqwravo"],["fjubadocdwaygs"],["x","a","ulqocaijhezwfr","zshbwqdhx"],["peaqbonzgl"],["pcfpppaxsxtpixd","ulqocaijhezwfr","hyxnrujrqykzhizm"],["a","ulqocaijhezwfr","hyxnrujrqykzhizm"],["a","rahimgtlopffbwdg"],["zshbwqdhx"],["fjubadocdwaygs","peaqbonzgl","brgjopmm","x"],["hyxnrujrqykzhizm"],["jmhobexvmmlyyzk","a","ulqocaijhezwfr"],["peaqbonzgl","x","a","ulqocaijhezwfr","zshbwqdhx"],["mf","pcfpppaxsxtpixd"],["fjubadocdwaygs","ulqocaijhezwfr"],["fjubadocdwaygs","x","a"],["zezdb","hyxnrujrqykzhizm"],["ccwfthnjt","a"],["fjubadocdwaygs","zezdb","a"],[],["peaqbonzgl","ccwfthnjt","hyxnrujrqykzhizm"],["xtadkauiqwravo","hyxnrujrqykzhizm"],["peaqbonzgl","a"],["x","a","hyxnrujrqykzhizm"],["zshbwqdhx"],[],["fjubadocdwaygs","mf","pcfpppaxsxtpixd","zshbwqdhx"],["pcfpppaxsxtpixd","a","zshbwqdhx"],["peaqbonzgl"],["peaqbonzgl","x","ulqocaijhezwfr"],["ulqocaijhezwfr"],["x"],["fjubadocdwaygs","peaqbonzgl"],["fjubadocdwaygs","xtadkauiqwravo"],["pcfpppaxsxtpixd","zshbwqdhx"],["peaqbonzgl","brgjopmm","pcfpppaxsxtpixd","a"],["fjubadocdwaygs","x","mf","ulqocaijhezwfr"],["jmhobexvmmlyyzk","brgjopmm","rahimgtlopffbwdg","hyxnrujrqykzhizm"],["x","ccwfthnjt","hyxnrujrqykzhizm"],["hyxnrujrqykzhizm"],["peaqbonzgl","x","xtadkauiqwravo","ulqocaijhezwfr","hyxnrujrqykzhizm"],["brgjopmm","ulqocaijhezwfr","zshbwqdhx"],["peaqbonzgl","pcfpppaxsxtpixd"],["fjubadocdwaygs","x","a","zshbwqdhx"],["fjubadocdwaygs","peaqbonzgl","x"],["ccwfthnjt"]]
req_skills=["zp","jpphhnhwpw","pscleb","arn","acrsxqvus","fseqih","fpqbjbbxglivyonn","cjozlkyodt","mvtwffgkhjrtibto","kumdvfwsvrht","i","s","ucr","oo","yqkqkhhhwngyjrg","odiwidzqw"]
people=[["acrsxqvus"],["zp"],[],["fpqbjbbxglivyonn"],[],[],["kumdvfwsvrht"],[],["oo"],[],["fseqih"],[],["arn"],[],[],["yqkqkhhhwngyjrg"],[],[],[],["kumdvfwsvrht"],["s"],[],[],["zp","ucr"],[],["pscleb"],[],[],[],[],[],[],[],["jpphhnhwpw"],[],[],[],["oo"],[],["i"],["pscleb"],[],[],[],[],[],[],["i"],[],["mvtwffgkhjrtibto","odiwidzqw"],[],["cjozlkyodt","odiwidzqw"],["arn"],[],[],["acrsxqvus"],[],[],[],["ucr"]]
x=Solution()
print(x.smallestSufficientTeam(req_skills,people))