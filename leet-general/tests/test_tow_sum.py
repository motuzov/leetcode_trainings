from leet_general.list_input import tow_sum, tow_sum_one_pass
from typing import List


def test_two_sum():
    assert tow_sum([1, 2, 7, 11, 15], 9) == [1, 2]
    assert tow_sum([-1, -2, -3, -4, -5], -8) == [2, 4]
    assert tow_sum([1, 3, 4, 2], 6) == [2, 3]


def test_two_sum_one_pass():
    assert tow_sum_one_pass([1, 2, 7, 11, 15], 9) == [1, 2]
    assert tow_sum_one_pass([-1, -2, -3, -4, -5], -8) == [2, 4]
    assert tow_sum_one_pass([1, 3, 4, 2], 6) == [2, 3]
    assert tow_sum_one_pass([2, 7, 11, 15], 9) == [0, 1]
