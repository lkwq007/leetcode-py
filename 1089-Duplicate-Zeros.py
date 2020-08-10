class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # 0<=arr[i]<=9
        ptr=0
        flag=False
        for i in range(len(arr)):
            arr[i]|=(arr[ptr]&0xf)<<4
            if arr[ptr]&0xf==0:
                if flag:
                    ptr+=1
                    flag=False
                else:
                    flag=True
            else:
                ptr+=1
        for i in range(len(arr)):
            arr[i]=arr[i]>>4