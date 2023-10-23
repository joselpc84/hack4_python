"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    r = 6
    while (r > 0):
        result.append(r-1)
        r-=1
    return result  