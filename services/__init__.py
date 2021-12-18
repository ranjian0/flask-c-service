from typing import List
from pathlib import Path
from ctypes import CDLL, c_double

class Service:
    lib_name = None

    def __init__(self):
        if self.lib_name:
            self.library = CDLL(str(
                Path(__file__).parent.joinpath(self.lib_name)
            ))

class SumService(Service):
    lib_name = "sum.so"

    def sum(self, nums: List[float]):
        array = (c_double * len(nums))(*nums)
        self.library.sum.restype = c_double
        return self.library.sum(array, len(nums))