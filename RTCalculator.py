import numpy as np
from math import factorial
import scipy
from scipy import signal
"""
This is a simple algorithm that calculates the RT of a set of data. To do that you need at least 8 days.
Credits to Robert Koch Institut.
"""
def rki(cases):
    sum1 = 0
    sum2 = 0
    smooth_cases = signal.savgol_filter(cases, 15, 3)
    for case in smooth_cases[len(cases)-8:len(cases)-4]:
        sum1 += case
    for case in smooth_cases[len(cases)-4:len(cases)]:
        sum2 += case

    return abs(round(1.382*sum2/sum1, 2))
