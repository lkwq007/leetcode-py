class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_shift=minutes/60.0*5.0
        if hour==12:
            hour=0
        hour_exact=hour*5.0+hour_shift
        diff=abs(minutes-hour_exact)
        angle=6.0*diff
        return min(angle,360-angle)