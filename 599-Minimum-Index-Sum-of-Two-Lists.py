class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        record={}
        for i in range(len(list1)):
            record[list1[i]]=i
        ret=len(list1)+len(list2)
        lst=[]
        for i,item in enumerate(list2):
            if item in record:
                if record[item]+i<ret:
                    ret=record[item]+i
                    lst=[item]
                elif record[item]+i==ret:
                    lst.append(item)
        return lst