from . import zStats

def nePopulationTestGivenStats(sampMean,popMean,std,num,alpha):
	print ""
	print "Null Hypothesis: mu = "+str(popMean)
	print "Alternative Hypothesis: mu != "+str(popMean)
	zscore = zStats.zStatistic(sampMean,popMean,std,num)
	print "Z-Score: "+str(zscore)
	pscore = zStats.notEqualP(zscore)
	print "P-Score: "+str(pscore)
	if pscore < alpha:
		print "We reject the null hypothesis."
	else:
		print "We keep the null hypothesis."
	print""

def gtPopulationTestGivenStats(sampMean,popMean,std,num,alpha):
	print ""
	print "Null Hypothesis: mu = "+str(popMean)
	print "Alternative Hypothesis: mu > "+str(popMean)
	zscore = zStats.zStatistic(sampMean,popMean,std,num)
	print "Z-Score: "+str(zscore)
	pscore = zStats.greaterThanP(zscore)
	print "P-Score: "+str(pscore)
	if pscore < alpha:
		print "We reject the null hypothesis."
	else:
		print "We keep the null hypothesis."
	print ""
