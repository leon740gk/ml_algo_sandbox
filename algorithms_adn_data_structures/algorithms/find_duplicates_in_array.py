# https://www.youtube.com/watch?v=kRrSeAZRD6E
from typing import List


def find_duplicates(nums: List[int]) -> List[int]:
    result = []
    for num in nums:
        num = abs(num)
        if nums[num - 1] > 0:
            nums[num - 1] *= -1
        else:
            result.append(num)

    return result
