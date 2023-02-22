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
    return           # returns decision tree
    
def DT_train_helper(data, remaining_features):

    i = 0
    num_rows, num_cols = data.shape
    num_features = num_cols - 1 
    
    # count remaining number of features
    i = 0
    num_features_remaining = 0
    while i < num_features:      
        if remaining_features[i] == 1:
            num_features_remaining += 1
            i += 1
            
    # count number of yes labels and number of no labels
    num_yes = 0
    num_no = 0
    i = 0
    while i < num_rows:
        if data[i][num_features] == 1:
            num_yes += 1
        else:
            num_no += 1
        i += 1
        
    # make guess based on majority of labels
    if (num_yes > num_no):
        guess = yes
    else:
        guess = no
        
    if num_yes == 0 or num_no == 0:     # if unambiguous
        return LEAF(guess)
    elif num_features_remaining == 0:
        return LEAF(guess)
    else:
        return 

    print("end") 
    print (NODE(1, LEAF(guess), LEAF(guess)))
    return

def LEAF(guess):
    return [guess, [], []]

def NODE(feature, left, right):     #feature is int of feature index
    feature_node = [feature, left, right]
    return feature_node