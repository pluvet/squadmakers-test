from dataclasses import dataclass
from fastapi import HTTPException
from typing import List
from source.domain.math import mcm, add_one

@dataclass
class MathService:
    """joke actions"""

    @staticmethod
    def mcm(nums: List[int])-> dict:
        """this function gets an mcm"""     
        mcm_number = {"mcm": mcm(nums)}

        return mcm_number
    
    @staticmethod
    def add_one(num: int)-> dict:
        """this function adds 1 to a number"""
        num = {"num": add_one(num)}
        
        return num