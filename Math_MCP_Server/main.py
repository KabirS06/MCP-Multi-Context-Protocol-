from __future__ import annotations
from fastmcp import FastMCP

mcp=FastMCP(name='Ramanujan')

def _as_number(x):
    if isinstance(x, (int,float)):
        return float(x)
    if isinstance(x, str):
        return float(x.strip())
    raise TypeError("Expected a Number! (int /float or numeric string)")

@mcp.tool
async def add(a:float , b :float)-> float:
    """Return the addition of two numbers """
    return (_as_number(a)+_as_number(b))

@mcp.tool
async def subtract(a:float , b:float )->float:
    """Returns the subtraction Two Numbers""" 
    return(_as_number(a)-_as_number(b))

@mcp.tool
async def multiply(a:float , b:float)->float:
    """Return the multiplications of two numbers """
    return (_as_number(a)*_as_number(b))

@mcp.tool
async def divison(a:float , b:float)->float:
    """Returns the divison of two numbers """
    return (_as_number(a)/_as_number(b))

@mcp.tool
async def power(a: float , b:float)->float:
    """Returns the power of a number """
    return(_as_number(a)**_as_number(b))
