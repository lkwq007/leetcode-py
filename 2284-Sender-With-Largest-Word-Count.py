class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        record={}
        for msg,name in zip(messages,senders):
            record[name]=record.get(name,0)+len(msg.split(" "))
        lst=[(msg,name) for name,msg in record.items()]
        lst.sort()
        return lst[-1][1]
