from . import simpleStats
import scipy.stats as stats
import math

#Function: functionName
#Arguements: arg - arg description
#Description: description

def marginOfError(confidenceIntPercent, std, n):
	percent = ((1-confidenceIntPercent)/2.0)+confidenceIntPercent
	return stats.norm.ppf(percent)*(std/(n ** .5))

def confidenceInterval(mean, confidenceIntPercent, std, n):
	ME = marginOfError(confidenceIntPercent, std, n)
	return (mean-ME,mean+ME)

def sampleSizeN(confidenceIntPercent,std,ME):
	percent = ((1-confidenceIntPercent)/2.0)+confidenceIntPercent
	return (((stats.norm.ppf(percent)*std)/ME)**2)

def zStatistic(sampMean, popMean, std, num):
	top = sampMean-popMean
	bottom = std / (num ** .5)
	return top / bottom

def notEqualP(zscore):
	absZ = math.fabs(zscore)
	return 2*(1-stats.norm.cdf(absZ))

def greaterThanP(zscore):
	return (1-stats.norm.cdf(zscore))

