class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        n = len(intervals)
        # sort the intervals
        intervals.sort(key=lambda x:x[0])
        # merged intervals
        merged = [intervals[0]]
        for current in intervals[1:]:
            lastMerged = merged[-1]
            if current[0] <= lastMerged[1]:
                lastMerged[1] = max(lastMerged[1],current[1])
            else:
                merged.append(current)
        return merged