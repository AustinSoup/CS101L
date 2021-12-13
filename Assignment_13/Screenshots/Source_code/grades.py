import math

def total(values):
    sum = 0
    for value in values:
        sum += value
    return sum

def average(values):
    if len(values) == 0:
        return math.nan
    return sum(values) / len(values)


def median(values):
    list1 = sorted(values)
    if (len(values)) == 0:
        raise ValueError
    elif (len(values) % 2 == 0):
        median = (list1[(len(list1)//2)] + list1[(len(list1)//2) - 1]) / 2
        return median
    elif(len(values) % 1 == 0): 
        return list1[(len(list1)//2)]
