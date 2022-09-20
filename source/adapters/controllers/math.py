from typing import List
from fastapi import APIRouter, Request, Query
from fastapi.responses import JSONResponse
from source.services.math import MathService


math_router = APIRouter()
    
@math_router.get('/mcm')
async def mcm(nums: List[int] = Query(default=[2,4,6])) -> JSONResponse:
    """this function gets the mcm from a list of nums"""
    mcm_number = MathService.mcm(nums=nums)

    return JSONResponse(mcm_number, status_code=200)

@math_router.get('/add')
async def add_one(num: int = Query(default=4)) -> JSONResponse:
    """this function gets a number and returns it with +1"""
    num = MathService.add_one(num=num)

    return JSONResponse(num, status_code=200)
