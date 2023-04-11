import math
import random
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


# FOR THIS YOUTRYIT YOU MUST COMPLETE THIS FUNCTION!
def knearest(X_train, y_train, predict):

    # this is the index to the iris that is closest
    # to the iris we are trying to predict
    # the goal of this function is to find this
    # index...
    min_sample_idx = 0
    min_distance = 10000
    # for each iris in the training set...
    for i1 in range(0, len(X_train)):
        # calculate the distance between the
        # iris in the training set at location i1
        # and the iris you are trying to predict...
        distance = 0
        for x in range(3):
            distance = distance + abs(X_train[i1][x] - predict[x])
            # if the difference between this iris and the
            # iris you are trying to predcict
            # is smaller than the smallest distance you have
            # found so far, make this distance the smallest so far
            # and store the index for this iris in min_sample_idx...
        if(distance < min_distance):
            min_distance = distance
            min_sample_idx = i1
                
            # Here I am just setting the closest iris to a random
            # sample in the training set, this will create a working
            # knearest function, but it won't score very well!!
            # when you complete this function you should be setting
            # this index to the training set iris that really is the closest
            # to the iris you are trying to predict!!
            

            # refer to this (https://www.mathopenref.com/coorddist.html)
            # in case you forgot how to calculate two
            # points in a multi-dimenaional space...

    # return the iris that is closest to this iris
    # we are tryig to predict...
    return y_train[min_sample_idx]


#YOU SHOULD NOT EDIT THIS FUNCTION
def trainAndScore(randomState):
    iris_dataset = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris_dataset['data'], iris_dataset['target'], random_state=randomState)

    total = 0
    correct = 0
    for i in range(0, len(X_test)):
        ans = knearest(X_train, y_train, X_test[i])
        total = total + 1
        if ans == y_test[i]:
            correct = correct + 1
    return correct / total


# This trains a ML model and scores it using
# a random state value, try it with different
# values for the random state value and you should
# occasionally get different scores. This demonstrates
# that the quality of the model can depend on how you
# split the data into train and test sets.
score = trainAndScore(0)
print(round(score, 2))
