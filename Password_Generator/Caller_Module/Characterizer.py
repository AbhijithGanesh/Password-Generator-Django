from .Randomizer import convertor
from .dataset import caller

a = caller()
def supplier():
    global a
    set1,set2, set3, set4 = a
    return convertor(set1),convertor(set2), convertor(set3),convertor(set4)
