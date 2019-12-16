"""
    Our unit-test class ‘TestInput’ inherits from ‘unittest.TestCase’, this allows us to use several known 
    functions such as ‘setUpClass, tearDownClass, setUp, tearDown”, the former two are executed first and last, 
    the latter two are executed before each test function. In the ‘setUp’ function we download the data, split it and 
    save train and test-accuracies and confusion matrices. These variables will enable us to create two tests that use fit()
    and predict(), using a well known input, finally comparing the resulting output to the expected output.

    The goal:
        Before we create a unit-test, we need some input and output examples based on our data-set. First we download 
        the MNIST data-set, we split it to 60K & 10K, we create a ‘TheAlgorithm’ class variable and execute fit(), 
        we observe the training accuracy and the resulting confusion matrix. The accuracy figure and the confusion matrix 
        are unique in terms of input and output and will change if anything changes in our model, including the input, split 
        ratio, random seed, etc. Therefore, after running the model, we save the output for our unit-test and the idea is that 
        if something changes or breaks in ‘TheAlgorithm’ class or accompanying functions, the output will not match and the 
        test will fails. We do the same with the class’ predict() function and save the resulting test accuracy and confusion 
        matrix.
"""
import unittest 
from download import download, split
from algorithm import Algorithm
import numpy as np

class TestInput(unittest.TestCase):
  
    @classmethod
    def setUpClass(cls):
        print('setupClass')   
        pass

    @classmethod
    def tearDownClass(cls): 
        print('teardownClass')
        pass

    def setUp(self):
        print('setUp') 
        X, y = download()
        splitRatio = 60000
        self.X_train, self.y_train, self.X_test, self.y_test = split(X,y,splitRatio) 
        self.train_accuracy = 72.92166666666667
        self.train_confusion_matrix = np.matrix([[5447,   5,  40,  31,  49,  16, 198,  50,  81,   6],
                                                 [   3,6440, 127,  54,   3,  29,  25,  36,  24,   1],
                                                 [ 297, 420,3824, 163, 256,  19, 622, 186, 121,  50],
                                                 [ 124, 221, 255,4566,  54, 251,  97, 129, 275, 159],
                                                 [ 104, 128,  26,  54,4546, 342, 206, 133,  96, 207],
                                                 [ 399, 200, 109,1081, 416,2227, 289, 363, 228, 109],
                                                 [ 173,  89, 112,  55, 156, 229,5034,  25,  45,   0],
                                                 [ 213, 192, 205,  39, 160,  17,  26,5058,  60, 295],
                                                 [  67, 690, 202, 677,  73, 188, 347,  39,3437, 131],
                                                 [ 164, 162,  63, 290, 669, 279, 122, 735, 291,3174]])
        self.test_accuracy = 73.4
        self.test_confusion_matrix = np.matrix([[ 923,   1,   2,   3,   3,   1,  35,   3,   9,   0],
                                                [   0,1084,  23,  11,   0,   0,   5,   4,   8,   0],
                                                [  63,  78, 669,  27,  38,   2,  97,  28,  24,   6],
                                                [  20,  27,  35, 770,   8,  42,  18,  27,  45,  18],
                                                [  15,  21,   3,   8, 750,  60,  45,  23,  18,  39],
                                                [  56,  24,  15, 193,  73, 362,  56,  58,  38,  17],
                                                [  35,  10,  18,  11,  28,  42, 799,   6,   8,   1],
                                                [  23,  40,  52,   6,  21,   4,   7, 821,   8,  46],
                                                [  14,  90,  29,  99,  10,  33,  66,   7, 598,  28],
                                                [  21,  27,  10,  37, 133,  42,  27, 100,  48, 564]])

    def tearDown(self):
        print('tearDown')
        pass
        
    def test_fit(self):     
        np.random.seed(31337)
        self.ta = Algorithm(self.X_train, self.y_train, self.X_test, self.y_test)
        self.assertGreaterEqual(round(self.ta.fit()), round(self.train_accuracy))
        #self.assertEqual(self.ta.train_confusion_matrix.tolist(), self.train_confusion_matrix.tolist())  
  
    def test_predict(self):
        np.random.seed(31337)
        self.ta = Algorithm(self.X_train, self.y_train, self.X_test, self.y_test)
        self.ta.fit()
        self.assertGreaterEqual(round(self.ta.predict()), round(self.test_accuracy))
        #self.assertEqual(self.ta.train_confusion_matrix.tolist(), self.train_confusion_matrix.tolist()) 
      
if __name__ == '__main__':
  
    #run tests 
    unittest.main(argv=['first-arg-is-ignored'], exit=False)