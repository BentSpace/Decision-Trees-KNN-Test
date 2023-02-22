KNN_test

This function takes 5 parameters
X_train - A 2D array of training samples
Y_train - An array of labels for those training samples
X_test - A 2D array of test samples
Y_test - An array of labels for those test samples
K - The number of nearest neighbors to compare to

The function first creates a 2D array which holds all the training data along with their labels, along with space to hold the distances to a test point.  It then runs through each test point calculating the distance to each of the training points and saves it in the array, S.  It then sorts the array with the close test points at the top.  It then sums up the label for the K closest point to the test point and make a prediction based on the sign of that sum.  At the end it calculates it accuracy based on how many it predicted correctly.


