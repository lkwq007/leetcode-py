class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        ret=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        base=5
        cur_day=15
        cur_month=8
        cur_year=2022
        days=[31,30,31]