"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        temp = []

        for i in intervals:
            start, end = i.start, i.end

            for i2 in temp:
                old_start, old_end = i2.start, i2.end
                if start < old_end and old_start < end:
                    return False

            temp.append(i)

        return True