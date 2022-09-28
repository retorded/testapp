from calculator import calc
from filters import geofilter


def run():
    print("One plus one is: ", calc.sumtwointegers(1, 1))
    print("N50 is in northern hemisphere: ", geofilter.is_north_hemisphere(50))


# Should this be here or in __main__ of this dir?
'''
if __name__ == '__main__':
    run()
'''