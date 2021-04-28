#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    return the list of all the delays (float values). The list of the
    delays should be in ascending order without using sort() because of
    concurrency.
    """
    list_float: List[float] = []
    for i in range(n):
        list_float.append(await wait_random(max_delay))
    return sorted(list_float)
