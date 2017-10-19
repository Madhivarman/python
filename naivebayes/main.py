# important libraries we need

import pandas as pd 
import numpy as ny 

#for preprocessing the data
#from sklearn.preprocessing import Imputer
from sklearn import preprocessing

#to split dataset into train and test
from sklearn.cross_validation import train_test_split

#to model Gaussian Naive Bayes
from sklearn.naive_bayes import GaussianNB

#to calculate accuracy of the model
from sklearn.metrics import accuracy_score


#data loading
#'*, * delimiter is to show delete the spaces'
df = pd.read_csv('sensus.data',header = None, delimiter=' *, *', engine='python')

df.columns = ['age', 'workclass', 'fnlwgt', 'education', 'education_num',
                    'marital_status', 'occupation', 'relationship',
                    'race', 'sex', 'capital_gain', 'capital_loss',
                    'hours_per_week', 'native_country', 'income']

#to handle the missing data
print(df.isnull().sum())

print("-------------------------")
print ("finding missing values")
print()
# to check whether any categorical value contains ? in it or not
for value in ['workclass','education',
          'marital_status', 'occupation',
          'relationship','race', 'sex',
          'native_country', 'income']:

          print value,":",sum(df[value] == '?')

#before duplicating
f = open("before_duplicating.txt","w")
f.write(str(df))
f.close()

#duplicate

duplicate_df = df

#summary statistics
duplicate_df.describe(include='all')

#impute the missing values
for value in ['workclass', 'education',
          'marital_status', 'occupation',
          'relationship','race', 'sex',
          'native_country', 'income']:

          duplicate_df[value].replace(['?'],[duplicate_df.describe(include='all')[value][2]],inplace='True')

#missing value is now filled
#after missing field is now replaced
f = open("after_filled.txt","w")
f.write(str(duplicate_df))
f.close()


#encoding data into binary format
le = preprocessing.LabelEncoder()
workclass_cat = le.fit_transform(df.workclass)
education_cat = le.fit_transform(df.education)
marital_cat = le.fit_transform(df.marital_status)
occupation_cat = le.fit_transform(df.occupation)
relationship_cat = le.fit_transform(df.relationship)
race_cat = le.fit_transform(df.race)
sex_cat = le.fit_transform(df.sex)
native_country_cat = le.fit_transform(df.native_country)


#initializing into duplicate dataset
duplicate_df['workclass_cat'] = workclass_cat
duplicate_df['education_cat'] = education_cat
duplicate_df['marital_cat'] = marital_cat
duplicate_df['occupation_cat'] = occupation_cat
duplicate_df['relationship_cat'] = relationship_cat
duplicate_df['race_cat '] = race_cat
duplicate_df['sex_cat '] = sex_cat
duplicate_df['native_country_cat'] = native_country_cat


# drop categorical columns dataframe
dummy_fields = ['workclass', 'education', 'marital_status', 
                  'occupation', 'relationship', 'race',
                  'sex', 'native_country']

duplicate_df = duplicate_df.drop(dummy_fields,axis = 1)

duplicate_df = duplicate_df.reindex_axis(['age', 'workclass_cat', 'fnlwgt', 'education_cat',
                                    'education_num', 'marital_cat', 'occupation_cat',
                                    'relationship_cat', 'race_cat', 'sex_cat', 'capital_gain',
                                    'capital_loss', 'hours_per_week', 'native_country_cat', 
                                    'income'],axis = 1)

f = open("final_phase.txt","w")
f.write(str(duplicate_df))
f.close()

#standardization


num_features = ['age', 'workclass_cat', 'fnlwgt', 'education_cat', 'education_num',
                'marital_cat', 'occupation_cat', 'relationship_cat', 'race_cat',
                'sex_cat', 'capital_gain', 'capital_loss', 'hours_per_week',
                'native_country_cat']

scaled_features = {}

for each in num_features:
    mean, std = duplicate_df[each].mean(), duplicate_df[each].std()
    scaled_features[each] = [mean, std]
    duplicate_df.loc[:, each] = (duplicate_df[each] - mean)/std


#writing into external file
f = open("duplicate_sensus.txt","w")
f.write(str(duplicate_df))
f.close()

#to check if the data has null values
print("Null values:")
print("-----------------------------")
print(duplicate_df.isnull().sum())
#data slicing
#split train and test set
#Using above code snippet, we have divided the data into features and target set. The feature set consists of 14 columns 
features = duplicate_df.values[:,:14]
target = duplicate_df.values[:,14]


#The features_train & target_train consists of training data and the features_test & target_test consists of testing data.
features_train, features_test, target_train, target_test = train_test_split(features,
                                                                            target, test_size = 0.33, random_state = 10)

#gaussian model
clf = GaussianNB()
clf.fit(features_train, target_train)
target_pred = clf.predict(features_test)

#accuracy calculation
print("Accuracy for our model is:")
print("-------------------------------")
print(accuracy_score(target_test,target_pred,normalize = True))