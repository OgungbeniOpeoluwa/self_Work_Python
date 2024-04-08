import sys
from builtins import input


def returnValueInAList():
    value = input()
    values = value.split(",")
    result = {n: int(n) * int(n) for n in values}
    return result
