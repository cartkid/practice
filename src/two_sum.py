# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return_me: List[int] = []

        for idx, item in enumerate(nums):
            if item > target:
                continue
            temp_value = target - item

            try:
                temp_value_index = nums.index(temp_value, idx + 1)
                return_me.append(idx)
                return_me.append(temp_value_index)
                break
            except ValueError:
                continue

        return return_me
