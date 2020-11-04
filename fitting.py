import numpy as np

def pol(x, y):
    m, q = np.polyfit(x, y, 1)
    f = {
        'x': x,
        'm': m,
        'q': q
    }
    return f

def pol_just_slope(x, y):
    return pol(x,y)['m']

def pol_just_ins(x, y):
    return pol(x,y)['q']