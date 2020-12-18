class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        record={}
        for item in record:
            record[item]=record.get(item,0)+1
        