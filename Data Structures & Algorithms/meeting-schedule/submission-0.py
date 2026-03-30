"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n=len(intervals)
        for i in range(n):
            m1 = intervals[i]
            for j in range(i+1,n):
                m2=intervals[j]
                if max(m1.start,m2.start)<min(m1.end,m2.end):
                    return False
        return True
