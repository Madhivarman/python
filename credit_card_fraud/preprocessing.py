# libraries

import pandas as pd 
import numpy as np 
from sklearn.preprocessing import Imputer
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
import csv

#load the file
TRAINING_SET = 'dataset/test.csv'
TESTING_SET = 'dataset/train.csv'

training_file = pd.read_csv(TRAINING_SET)
testing_file = pd.read_csv(TESTING_SET)

#review the csv file

print("No.of.Rows and columns in training set:",training_file.shape)
print("NO.of.Rows and columns in testing set:",testing_file.shape)

#to check whethere there is any null values
train_set_null = training_file.isnull().sum()
testing_set_null = testing_file.isnull().sum()

#print("check null values:",train_set_null)

# there is sum null values in the dataset 
# to train the model there should be no null values in the dataset
# fill those null values with default value

# make a dupilcate copy of original dataframe for training_set

duplicate_training_file = training_file
duplicate_testing_file = testing_file

for values in ['cat_var_1','cat_var_3','cat_var_6','cat_var_8'] : 

	duplicate_training_file = duplicate_training_file.fillna("?")  #there is no empty value in this dataset

for values in ['cat_var_1','cat_var_3','cat_var_8']:

	duplicate_testing_file = duplicate_testing_file.fillna("?")

#impute the dataframe '?' with values

for values in ['cat_var_1','cat_var_3','cat_var_6','cat_var_8']:

	duplicate_training_file[values].replace(['?'],[duplicate_training_file[values][3]],inplace=True)

for values in ['cat_var_1','cat_var_3','cat_var_8']:

	duplicate_testing_file[values].replace(['?'],[duplicate_testing_file[values][2]],inplace=True)


#print(duplicate_training_file.iloc[1:16,10])

# storing the duplicate file as csv file
"""duplicate_training_file.to_csv('edited_dataset/train_set.csv',sep=',',encoding='utf-8')
duplicate_testing_file.to_csv('edited_dataset/test_set.csv',sep=',',encoding='utf-8')"""

#one hot encoding the values
#reading the fully filled datasets
df_train_set = pd.read_csv('edited_dataset/test_data.csv')
df_test_set = pd.read_csv('edited_dataset/train_data.csv')

train_set_header = ['cat_var_1','cat_var_2','cat_var_3','cat_var_4','cat_var_5','cat_var_6',
        'cat_var_7','cat_var_8','cat_var_9','cat_var_10','cat_var_11','cat_var_12','cat_var_13',
        'cat_var_14','cat_var_15','cat_var_16','cat_var_17','cat_var_18']


clfs = {c:LabelEncoder() for c in train_set_header}

for col,cls in clfs.items():

	 df_train_set[col] = clfs[col].fit_transform(df_train_set[col])
	 df_test_set[col] = clfs[col].fit_transform(df_test_set[col])


#storing as new  file
"""df_train_set.to_csv('edited_dataset/en_train_set.csv',sep=',',encoding='utf-8')
df_test_set.to_csv('edited_dataset/en_test_set.csv',sep=',',encoding='utf-8')"""

#now read the encoded dataset
en_train_set = pd.read_csv('edited_dataset/en_test_data.csv')
en_test_set = pd.read_csv('edited_dataset/en_train_data.csv')
#now specifying the column we want to standardize

std_train_header = ['num_var_1','num_var_5','num_var_6','num_var_7','cat_var_1','cat_var_2','cat_var_3','cat_var_6',
					'cat_var_7','cat_var_8','cat_var_9','cat_var_10','cat_var_11','cat_var_12','cat_var_13','cat_var_14']


#standardize the data
#create a dictionary
special_features= {}

#for en_train_set data
for each in std_train_header:
	mean,std = en_train_set[each].mean(),en_train_set[each].std()
	special_features[each] = [mean,std]
	en_train_set.loc[:,each] = (en_train_set[each]-mean)/std

#for en_test_set data

for each in std_train_header:
	mean,std = en_test_set[each].mean(),en_test_set[each].std()
	special_features[each] = [mean,std]
	en_test_set.loc[:,each] = (en_test_set[each]-mean)/std

#storing standardize model in the seperate folder
en_train_set.to_csv('final_dataset/train_set.csv',sep=',',encoding='utf-8')
en_test_set.to_csv('final_dataset/test_set.csv',sep=',',encoding='utf-8')
