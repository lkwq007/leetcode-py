class Solution:
    def average(self, salary: List[int]) -> float:
        # unique ints
        min_val=salary[0]
        max_val=salary[0]
        acc=0
        for item in salary:
            acc+=item
            min_val=min(min_val,item)
            max_val=max(max_val,item)
        return (acc-max_val-min_val)/(len(salary)-2)