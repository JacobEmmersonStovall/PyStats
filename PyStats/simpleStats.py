#Function: mean(x)
#Arguements: x - Array of values
#Description: Returns the mean of the array of values
def mean(x):
    total = 0.0
    for num in x:
        total = total+num
    if x == []:
        return 0
    else:
        return (total/len(x))

#Function: std(x)
#Arguements: x - Array of values
#Description: Returns the standard deviation for the array of values
def std(x):
    sumation = 0.0
    sampMean = mean(x)
    for num in x:
        sumation = sumation + ((num-sampMean)**2)
    whole = sumation/(len(x)-1)
    return (whole ** .5)

#Function: std(x)
#Arguements: x - Array of values
#Description: Returns the variance for the array of values
def variance(x):
    return (std(x)**2)

#Function: zScore(experimentalValue, dataSet)
#Arguements:experimentalValue - Point on the xAxis that we are getting
#                               a z-score for
#           dataSet - Array of Values
#Description:Gets z-Score for a certain experimental value based on
#            a data set
def zScore(experimentalValue, dataSet):
    top = experimentalValue - mean(dataSet)
    bottom = std(dataSet)
    return top/bottom

#Function: fac(n)
#Arguements: n -  An int value
#Description: Returns n!
def fac(n):
    value = 1
    if n <= 1:
        return value
    else:
        while(n > 1):
            value = value * n
            n = n-1
        return value

#Function: nCr(n,k)
#Arguements: n - Total number of items(int)
#            k - Number of items being chosen(int)
#Description: Returns n choose k
def nCr(n,k):
    top = fac(n)
    bottom = fac(n-k)*fac(k)
    return top/bottom

#Function: binomialProb(numT,numR,probOccur)
#Arguements: numT - Number of Trials
#            numR - Number of Successful Trials
#            probOccur - Probability of Success
#Description: Binomial Probability for numR successes
#             out of numT trials when the probability
#             of success is probOccur.
def binomialProb(numT,numR,probOccur):
    return nCr(numT,numR)*(probOccur**numR)*((1-probOccur)**(numT-numR))

#Function: binomialProbSummation(numT,numRLower,numRUpper,probOccur)
#Arguements: numT - Number of Trials
#            numRLower - Lowest Number of Successful Trials
#            numRUpper - Largest Number of Successful Trials
#            probOccur - Probability of Success
#Description: Summation of the binomial probabilities between
#             numRLower and numRUpper
def binomialProbSummation(numT,numRLower,numRUpper,probOccur):
    n = numRLower
    summation = 0.0
    while(n <= numRUpper):
        summation += binomialProb(numT,n,probOccur)
        n = n+1
    return summation

