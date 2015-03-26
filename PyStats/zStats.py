from . import simpleStats
import scipy.stats as stats

#Function: functionName
#Arguements: arg - arg description
#Description: description

def marginOfError(confidenceIntPercent, std, n):
	percent = ((1-confidenceIntPercent)/2.0)+confidenceIntPercent
	return stats.norm.ppf(percent)*(std/(n ** .5))

def confidenceInterval(mean, confidenceIntPercent, std, n):
	ME = marginOfError(confidenceIntPercent, std, n)
	return (mean-ME,mean+ME)