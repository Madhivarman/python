from decorator import my_logger, my_timer
from download import Normalize
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.linear_model import LogisticRegression
import numpy as np

class Algorithm(object):

    @my_logger
    @my_timer
    def __init__(self,X_train, y_train, X_test, y_test):
        self.X_train, self.y_train, self.X_test, self.y_test = X_train, y_train, X_test, y_test
    
    @my_logger 
    @my_timer 
    def fit(self):
        normalizer = Normalize()
        self.X_train, self.X_test = normalizer.normalize(self.X_train, self.X_test)
        train_samples = self.X_train.shape[0]
        self.classifier = LogisticRegression(
            C=50. / train_samples,
            multi_class='multinomial',
            penalty='l1',
            solver='saga',
            tol=0.1,
            class_weight='balanced',
            )
        self.classifier.fit(self.X_train, self.y_train)
        self.train_y_predicted = self.classifier.predict(self.X_train)
        self.train_accuracy = np.mean(self.train_y_predicted.ravel() == self.y_train.ravel()) * 100
        self.train_confusion_matrix = confusion_matrix(self.y_train, self.train_y_predicted)        
        return self.train_accuracy
    
    @my_logger
    @my_timer
    def predict(self):
        self.test_y_predicted = self.classifier.predict(self.X_test) 
        self.test_accuracy = np.mean(self.test_y_predicted.ravel() == self.y_test.ravel()) * 100 
        self.test_confusion_matrix = confusion_matrix(self.y_test, self.test_y_predicted)        
        self.report = classification_report(self.y_test, self.test_y_predicted)
        print("Classification report for classifier:\n %s\n" % (self.report))
        return self.test_accuracy


