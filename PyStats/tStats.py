from . import simpleStats
import scipy.stats as stats

def standardErrorForT(x):
    return (simpleStats.std(x)/(len(x)**.5))

def twoStandardErrorForT(x,y):
    SE = ((simpleStats.std(x)**2)/len(x))+((simpleStats.std(y)**2)/len(y))
    SE = SE ** .5
    return SE

def tscore(x,mu):
    top  = simpleStats.mean(x) - mu
    bottom = standardErrorForT(x)
    return top/bottom

def twoTScore(x,y,muUno=0,muDos=0):
    top = (simpleStats.mean(x)-simpleStats.mean(y))-(muUno-muDos)
    bottom = ((simpleStats.std(x)**2)/len(x))+((simpleStats.std(y)**2)/len(y))
    bottom = bottom ** .5
    return top/bottom
