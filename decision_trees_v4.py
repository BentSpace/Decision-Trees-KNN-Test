import numpy as np
import math
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
    num_yes_no_label = count_YN(data, num_features)
        
    # make guess based on majority of labels
    if (num_yes_no_label[0] > num_yes_no_label[1]):
        guess = yes
    else:
        guess = no
        
    if num_yes_no_label[0] == 0 or num_yes_no_label[1] == 0:     # if unambiguous
        return LEAF(guess)
    elif num_features_remaining == 0:
        return LEAF(guess)
    else:
        # Go thru each remaining feature and calulate IG
        i = 0
        IG = []     # list of IG's of corresponding to feature at index
        while i < num_features:
            if remaining_features[i] == 1:
                IG.append([i, calculate_IG(data, i)])
            i += 1
            print("IG: ", IG)
        print("hi")
        IG_sorted = sorted(IG, key=lambda l:l[1], reverse=True)      #sort based on IG
        highest_IG_feature_remaining = IG_sorted[0][1]
        no_subset = select_subset(data, highest_IG_feature_remaining, no)
    print("end") 
    print (NODE(1, LEAF(guess), LEAF(guess)))
    return

# calculate Information Gain on the feature index specified
def calculate_IG(data, feature): 
    num_rows, num_cols = data.shape
    labels = num_cols - 1
    num_yes_no = count_YN(data, feature)
    probability_yes = num_yes_no[0] / num_rows
    probability_no = num_yes_no[1] / num_rows
    entropy_whole_set = calculate_Entropy(data)
    yes_subset = select_subset(data, feature, yes)
    no_subset = select_subset(data, feature, no)
    entropy_yes_subset = calculate_Entropy(yes_subset)
    entropy_no_subset = calculate_Entropy(no_subset)
    IG = entropy_whole_set - (probability_no * entropy_no_subset + 
                                probability_yes * entropy_yes_subset)
    return IG

def calculate_Entropy(data): 
    if data.size == 0:
        return 0
    num_rows, num_cols = data.shape
    labels = num_cols - 1
    i = 0
    num_yes_no = count_YN(data, labels)
    probability_yes = num_yes_no[0] / num_rows
    probability_no = num_yes_no[1] / num_rows
    if probability_no == 0 or probability_yes == 0:
        return 0
    else:
        return (- probability_no * math.log(probability_no, 2) 
                - probability_yes * math.log(probability_yes, 2)) 
        
# count number of yes labels and number of no labels in column col
def count_YN(data, col):
    num_rows, num_cols = data.shape
    num_yes = 0
    num_no = 0
    i = 0
    while i < num_rows:
        if data[i][col] == 1:
            num_yes += 1
        else:
            num_no += 1
        i += 1
    return [num_yes, num_no]
    
# returns a subset of the data based on column specifief and yes or no
def select_subset(data, col, yn):
    num_rows, num_cols = data.shape
    i = 0
    temp_arr = []
    while i < num_rows:
        if data[i][col] == yn:
            temp_arr.append(data[i])
        i += 1
    return np.array(temp_arr)
    

def LEAF(guess):
    return [guess, [], []]

def NODE(feature, left, right):     #feature is int of feature index
    feature_node = [feature, left, right]
    return feature_node