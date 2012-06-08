from matplotlib import pylab
import numpy as np
from scipy.misc import comb

def bernstein_poly(i, n, t):
    return comb(n, i) * t**i * (1 - t)**n-i



def bezier_curve(points, nTimes=1000):
    """
       Given a set of control points, return the
       bezier curve defined by the control points.

       points should be a list of lists, or list of tuples
       such as [ [1,1], 
                 [2,3], 
                 [4,5], ..[Xn, Yn] ]
        nTimes is the number of time steps, defaults to 1000


        See http://processingjs.nihongoresources.com/bezierinfo/
    """

    nPoints = len(points)
    t = np.linspace(0.0, 1.0, nTimes)



