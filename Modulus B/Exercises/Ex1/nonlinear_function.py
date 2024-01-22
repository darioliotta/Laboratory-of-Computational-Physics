import numpy as np

# a nonlinear function of a 2d array x
def f(x,c=1):
    r=0
    if c==1:
        if x[0]>-30 and x[1]>-30 and x[0]+x[1] < 33:
            r=1
        if x[0]+x[1] > 50:
            r=1
    if c==2:
        if (np.sign(0.7*x[0]+0.3*x[1]+10))*np.cos(np.linalg.norm(x)/(2*np.pi))>0:
            r=1
    return r


def filename(s,TYPE=1):
    return "./DATA/"+s+"-for-DNN-"+str(TYPE)+".dat"
