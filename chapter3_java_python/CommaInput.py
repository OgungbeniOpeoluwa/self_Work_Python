import sys
from builtins import input



def returnValueInAList():
    value = input()
    values = value.split(",")
    result = list((lambda number: int(number) * int(number), values))
    return result

