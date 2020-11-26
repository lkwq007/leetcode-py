class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        record={}
        for i in range(len(pieces)):
            record[pieces[i][0]]=i
        idx=0
        while idx<len(arr):
            if arr[idx] in record:
                piece=pieces[record[arr[idx]]]
                for item in piece:
                    if item==arr[idx]:
                        idx+=1
                    else:
                        return False
            else:
                return False
        return True