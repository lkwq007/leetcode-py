class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        record=[0]*26
        base=ord("a")
        for item in target:
            record[ord(item)-base]+=1
        cnt=[0]*26
        for sticker in stickers:
            for item in sticker:
                cnt[ord(item)-base]=1
        for i in range(26):
            if record[i]>0 and cnt[i]==0:
                return -1