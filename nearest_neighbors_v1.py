import numpy as np
#import math as mh
from scipy.spatial import distance
#import random.randint as rr

def KNN_test(X_train,Y_train,X_test,Y_test,K):
    S = []
    N = len(Y_train)
    i = 1
    a = np.zeros((6,2))
    b = np.ones((6,1))
    c = np.hstack((a,b))
    Y_vert = Y_train.reshape(Y_train.shape[0],-1)
    new_col = np.zeros((N,1))
    # np.reshape(Y_train, (10,2))

    training_data = np.hstack((X_train, Y_vert))

    print (new_col)
    training_data = np.hstack((training_data, new_col))
    print (training_data)
    # print (c)
    # print (X_train)
    # print (training_data)
    # while i < N:

    
  
    # i = 0                              #array to stor distance to training example n
    # for sample in training_data:              #mearsure distance from test point to every 
    #     S [i] = distance.euclidean(sample, X_test[0])               #point in training data and store in S
    #     print (S[i])
    #     i += 1