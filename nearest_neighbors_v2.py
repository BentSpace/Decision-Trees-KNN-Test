import numpy as np
#import math as mh
from scipy.spatial import distance
#import random.randint as rr

def KNN_test(X_train,Y_train,X_test,Y_test,K):
    #S = []
    N = len(Y_train)
    i = 1

    Y_vert = Y_train.reshape(Y_train.shape[0],-1)
    new_col = np.zeros((N,1))
    # np.reshape(Y_train, (10,2))

    S = np.hstack((X_train, Y_vert))
    S = np.hstack((S, new_col))
    accuracy = 1.0
    number_correct_predictions = 0
    j = 0
    for test_point in X_test:
        i = 0  
        while i < N:
            S[i, 3] = distance.euclidean(X_train[i], test_point)
            i += 1
        #print (S)
        S_sorted = np.sort(S) 
        S_sorted = S[S[:, 3].argsort()]      #sort based of distance
        #print (S_sorted)
        i = 0
        sum = 0
        while i < K:
            sum += S_sorted[i, 2]
            i += 1
        if sum > 0:
            y_hat = 1               #y_hat is prediction
        else:
            y_hat = -1
        print (y_hat)
        if y_hat == Y_test[j]:
            number_correct_predictions += 1
        j += 1
    
    print (number_correct_predictions)
        
  
    #                             #array to stor distance to training example n
    # for sample in training_data:              #mearsure distance from test point to every 
    #     S [i] = distance.euclidean(sample, X_test[0])               #point in training data and store in S
    #     print (S[i])
    #     i += 1