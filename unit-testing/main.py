from download import download, split
from algorithm import Algorithm
import numpy as np

def main():
  X,y = download()
  print ('MNIST:', X.shape, y.shape)
  
  splitRatio = 60000
  X_train, y_train, X_test, y_test = split(X,y,splitRatio) 

  np.random.seed(31337)
  ta = Algorithm(X_train, y_train, X_test, y_test)
  train_accuracy = ta.fit()
  print()
  print('Train Accuracy:', train_accuracy,'\n') 
  print("Train confusion matrix:\n%s\n" % ta.train_confusion_matrix)
  
  test_accuracy = ta.predict()
  print()
  print('Test Accuracy:', test_accuracy,'\n') 
  print("Test confusion matrix:\n%s\n" % ta.test_confusion_matrix)


if __name__ == "__main__":
    main()