import numpy as np
#import math as mh
from scipy.spatial import distance
#import random.randint as rr

def KNN_test(X_train,Y_train,X_test,Y_test,K):
    N = len(Y_train)
    i = 1

    Y_vert = Y_train.reshape(Y_train.shape[0],-1)
    new_col = np.zeros((N,1))

    S = np.hstack((X_train, Y_vert))
    S = np.hstack((S, new_col))
    number_correct_predictions = 0
    j = 0
    for test_point in X_test:
        i = 0  
        while i < N:
            S[i, 3] = distance.euclidean(X_train[i], test_point)
            i += 1
        #S_sorted = np.sort(S) 
        S_sorted = S[S[:, 3].argsort()]      #sort based of distance
        i = 0
        sum = 0
        while i < K:
            sum += S_sorted[i, 2]
            i += 1
        if sum > 0:
            y_hat = 1               #y_hat is prediction
        else:
            y_hat = -1
        if y_hat == Y_test[j]:
            number_correct_predictions += 1
        j += 1
    accuracy = number_correct_predictions / len(Y_test)
    return accuracy
        
