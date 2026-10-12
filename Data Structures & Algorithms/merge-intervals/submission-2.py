class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        previous_start = intervals[0][0]
        previous_end = intervals[0][1]
        to_return = []
        to_return.append([previous_start, previous_end])
        for index in range(1, len(intervals)):
            start = intervals[index][0]
            end = intervals[index][1]
            if start <= previous_end:
                to_return.pop()
                to_return.append([previous_start, max(end, previous_end)])
                previous_end = max(end, previous_end)
            else:
                to_return.append([start, end])
                previous_start = start
                previous_end = end
        return to_return





        