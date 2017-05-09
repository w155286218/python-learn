
#################################################
# LogRegression: Logistic Regression
# Author : zouxy
# Date   : 2014-03-02
# HomePage : http://blog.csdn.net/zouxy09
# Email  : zouxy09@qq.com
#################################################

import LogRegression_alg as lg

def loadData():
    train_x = []
    train_y = []
    fileIn = open('F:\\python\\data_flie\\testSet.txt')
    for line in fileIn.readlines():
        lineArr = line.strip().split()
        train_x.append([1.0, float(lineArr[0]), float(lineArr[1])])
        train_y.append(float(lineArr[2]))
    return lg.mat(train_x), lg.mat(train_y).transpose()


## step 1: load data
print "step 1: load data..."
train_x, train_y = loadData()
test_x = train_x; test_y = train_y

## step 2: training...
print "step 2: training..."
opts = {'alpha': 0.01, 'maxIter': 20, 'optimizeType': 'smoothStocGradDescent'}
optimalWeights = lg.trainLogRegres(train_x, train_y, opts)

## step 3: testing
print "step 3: testing..."
accuracy = lg.testLogRegres(optimalWeights, test_x, test_y)

## step 4: show the result
print "step 4: show the result..."    
print 'The classify accuracy is: %.3f%%' % (accuracy * 100)
lg.showLogRegres(optimalWeights, train_x, train_y) 