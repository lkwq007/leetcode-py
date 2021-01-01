class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        ret=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        base=5
        cur_day=1
        cur_month=1
        cur_year=2021
        days=[31,]