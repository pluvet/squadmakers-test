from typing import List
from math import gcd

def mcm(nums: List[int]) -> int:
    """calculates the mcm of a list"""
    lcm = 1

    for num in nums:
        lcm = lcm*num//gcd(lcm, num)

    return lcm

def add_one(number: int) -> int:
    """add one to a number"""
    return number + 1