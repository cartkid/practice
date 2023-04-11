from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Given an unsorted integer array nums, return the smallest missing positive integer.
        # You must implement an algorithm that runs in O(n) time and uses constant extra space.
        i: int = 0
        while i < len(nums):
            matching_position_and_value = nums[i] - 1
            # only bother sorting positive numbers less than the length of the list
            if (
                nums[i] > 0
                and nums[i] <= len(nums)
                and nums[i] != nums[matching_position_and_value]
            ):
                # swap matching_position_value with current i
                temp = nums[i]
                nums[i] = nums[matching_position_and_value]
                nums[matching_position_and_value] = temp
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
