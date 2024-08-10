from typing import List


def tow_sum(nums: List[int], target: int) -> List[int]:
    # t - x_i = x_j
    n_i = {n: i for i, n in enumerate(nums)}
    for i1, n in enumerate(nums):
        i2 = n_i.get(target - n, False)
        if i2 and i1 != i2:
            return [i1, i2]


def tow_sum_one_pass(nums: List[int], target: int) -> List[int]:
    # t - x_i = x_j
    n_i_map = {}
    for i2 in range(len(nums)):
        n = nums[i2]
        i1 = n_i_map.get(target - n, None)
        if i1 is not None:
            return [i1, i2]
        n_i_map[n] = i2
    return []
