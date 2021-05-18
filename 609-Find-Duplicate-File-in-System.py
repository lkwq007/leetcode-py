class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        record={}
        for path in paths:
            lst=path.split(" ")
            directory=lst[0]
            for file in lst[1:]:
                filename,content=file.split("(")
                if content not in record:
                    record[content]=[]
                record[content].append(directory+"/"+filename)
        return [v for v in record.values() if len(v)>1]