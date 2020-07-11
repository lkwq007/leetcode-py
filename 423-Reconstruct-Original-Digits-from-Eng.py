class Solution:
    def originalDigits(self, s: str) -> str:
        # this question is awful
        lst=["zero","one","two","three","four","five","six","seven","eight","nine"]
        record={}
        dictionary={}
        for i in range(10):
            word=lst[i]
            for item in word:
                if item not in dictionary:
                    dictionary[item]={}
                dictionary[item][i]=dictionary[item].get(i,0)+1
        for item in s:
            record[item]=record.get(item,0)+1
        def delete(num):
            word=lst[num]
            for item in word:
                if num in dictionary[item]:
                    del dictionary[item][num]
        ret=[]
        while len(record)>0:
            keys=list(dictionary.keys())
            for key in keys:
                if len(dictionary[key])==1:
                    num=list(dictionary[key].keys())[0]
                    if key in record:
                        cnt=record[key]
                        for i in range(cnt): ret.append(num)
                        word=lst[num]
                        for item in word:
                            record[item]-=cnt
                            if record[item]==0:
                                del record[item]
                    delete(num)
                    del dictionary[key]
                elif len(dictionary[key])==0:
                    del dictionary[key]
        return "".join(map(str,sorted(ret)))
            

x=Solution()
x.originalDigits("a")