from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        resulting_intervals: List[List[int]] = []
        intervals.sort()
        print(intervals)

        for interval in intervals:
            if len(resulting_intervals) == 0:
                resulting_intervals.append(interval)
            else:
                if Solution._should_merge(
                    interval, resulting_intervals[len(resulting_intervals) - 1]
                ):
                    resulting_intervals[
                        len(resulting_intervals) - 1
                    ] = Solution._merge_interval(
                        resulting_intervals[len(resulting_intervals) - 1], interval
                    )
                else:
                    resulting_intervals.append(interval)

        return resulting_intervals

    @staticmethod
    def _should_merge(interval_a: List[int], interval_b: List[int]) -> bool:
        return (
            (interval_b[0] >= interval_a[0] and interval_b[0] <= interval_a[1])
            or (interval_b[1] >= interval_a[0] and interval_b[1] <= interval_a[1])
            or (interval_a[0] >= interval_b[0] and interval_a[0] <= interval_b[1])
            or (interval_a[1] >= interval_b[0] and interval_a[1] <= interval_b[1])
        )

    @staticmethod
    def _merge_interval(interval_a: List[int], interval_b: List[int]) -> List[int]:
        return_me: List[int] = []
        return_me.append(
            interval_a[0] if interval_a[0] < interval_b[0] else interval_b[0]
        )
        return_me.append(
            interval_a[1] if interval_a[1] > interval_b[1] else interval_b[1]
        )
        return return_me
