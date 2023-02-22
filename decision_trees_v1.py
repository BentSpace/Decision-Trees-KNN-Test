import numpy as np
#import math as mh
#from scipy.spatial import distance
#import random.randint as rr

yes = 1
no = 0

def DT_train_binary(X,Y,max_depth):
    Y_vert = Y.reshape(Y.shape[0],-1)        # package labels with feature as
    DATA_SET = np.hstack((X, Y_vert))               # last column in 2D array

    num_rows, num_cols = X.shape
    num_features = num_cols
    REMAINING_FEATURES =  np.ones(num_features)# array of remaining features, 1 = remaining 0 = not
    print(REMAINING_FEATURES)
    DT_train_helper(DATA_SET, REMAINING_FEATURES)
    return

def DT_train_helper(data, remaining_features):
    num_yes = 0
    num_no = 0
    i = 0
    num_rows, num_cols = data.shape
    while i < num_rows:
        if data[i][num_cols - 1] == 1:
            num_yes += 1
        else:
            num_no += 1
        i += 1
    if (num_yes > num_no):
        guess = yes
    else:
        guess = no
    print("end") 
    return