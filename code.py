# -*- coding: utf-8 -*-
"""project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PWU6eqIubM1S75T2gwpEqOqthRFg87XW
"""

#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import drive
drive.mount('/content/drive')

# df = cv2.imread('/content/drive/My Drive/BTP/data.csv')
df = pd.read_csv('/content/drive/My Drive/BTP/data.csv')
df.head(7)

#Count the number of rows and columns in the data set
df.shape

#Count the empty (NaN, NAN, na) values in each column
df.isna().sum()

#Drop the column with all missing values (na, NAN, NaN)
#NOTE: This drops the column Unnamed
df = df.dropna(axis=1)

#Get the new count of the number of rows and cols
df.shape

#Get a count of the number of 'M' & 'B' cells
df['diagnosis'].value_counts()

#Visualize this count
sns.countplot(df['diagnosis'],label="Count")

#Look at the data types
df.dtypes

#Encoding categorical data values (
from sklearn.preprocessing import LabelEncoder
labelencoder_Y = LabelEncoder()
df.iloc[:,1]= labelencoder_Y.fit_transform(df.iloc[:,1].values)
print(labelencoder_Y.fit_transform(df.iloc[:,1].values))

sns.pairplot(df, hue="diagnosis")

df.head(5)

#Get the correlation of the columns
df.corr()

plt.figure(figsize=(20,20))
sns.heatmap(df.corr(), annot=True, fmt='.0%')

X = df.iloc[:, 2:31].values
Y = df.iloc[:, 1].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

print(f'The shape of Train data is {X_train.shape}')
print(f'The shape of Test data is {X_test.shape}')

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)



"""# K Nearest Neighbor"""

def models(X_train,Y_train):
  #Using KNeighborsClassifier
  from sklearn.neighbors import KNeighborsClassifier
  knn = KNeighborsClassifier(n_neighbors = 4, metric = 'minkowski', p = 2)
  knn.fit(X_train, Y_train)
  #print model accuracy on the training data.
  print('K Nearest Neighbor Training Accuracy:', knn.score(X_train, Y_train))
  return knn

model = models(X_train,Y_train)

def models(X_train,Y_train):
  #Using KNeighborsClassifier
  from sklearn.neighbors import KNeighborsClassifier
  knn = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
  knn.fit(X_train, Y_train)
  #print model accuracy on the training data.
  print('K Nearest Neighbor Training Accuracy:', knn.score(X_train, Y_train))
  return knn

model = models(X_train,Y_train)

def models(X_train,Y_train):
  #Using KNeighborsClassifier
  from sklearn.neighbors import KNeighborsClassifier
  knn = KNeighborsClassifier(n_neighbors = 6, metric = 'minkowski', p = 2)
  knn.fit(X_train, Y_train)
  #print model accuracy on the training data.
  print('K Nearest Neighbor Training Accuracy:', knn.score(X_train, Y_train))
  return knn

model = models(X_train,Y_train)

def models(X_train,Y_train):
  #Using KNeighborsClassifier
  from sklearn.neighbors import KNeighborsClassifier
  knn = KNeighborsClassifier(n_neighbors = 7, metric = 'minkowski', p = 2)
  knn.fit(X_train, Y_train)
  #print model accuracy on the training data.
  print('K Nearest Neighbor Training Accuracy:', knn.score(X_train, Y_train))
  return knn

model = models(X_train,Y_train)

def models(X_train,Y_train):
  #Using KNeighborsClassifier
  from sklearn.neighbors import KNeighborsClassifier
  knn = KNeighborsClassifier(n_neighbors = 8, metric = 'minkowski', p = 2)
  knn.fit(X_train, Y_train)
  #print model accuracy on the training data.
  print('K Nearest Neighbor Training Accuracy:', knn.score(X_train, Y_train))
  return knn

model = models(X_train,Y_train)

def models(X_train,Y_train):
  #Using KNeighborsClassifier
  from sklearn.neighbors import KNeighborsClassifier
  knn = KNeighborsClassifier(n_neighbors = 9, metric = 'minkowski', p = 2)
  knn.fit(X_train, Y_train)
  #print model accuracy on the training data.
  print('K Nearest Neighbor Training Accuracy:', knn.score(X_train, Y_train))
  return knn

model = models(X_train,Y_train)

def models(X_train,Y_train):
  #Using KNeighborsClassifier
  from sklearn.neighbors import KNeighborsClassifier
  knn = KNeighborsClassifier(n_neighbors = 10, metric = 'minkowski', p = 2)
  knn.fit(X_train, Y_train)
  #print model accuracy on the training data.
  print('K Nearest Neighbor Training Accuracy:', knn.score(X_train, Y_train))
  return knn

model = models(X_train,Y_train)



"""Confusion Matrix"""

from sklearn.metrics import confusion_matrix
#for i in range(len(model)):
i=0
cm = confusion_matrix(Y_test, model.predict(X_test))

TN = cm[0][0]
TP = cm[1][1]
FN = cm[1][0]
FP = cm[0][1]

print(cm)
print('Model[{}] Testing Accuracy = "{}!"'.format(i,(TP + TN) / (TP + TN + FN + FP)))
print()# Print a new line





"""# Naive Bayes"""

# M = df[df.diagnosis == "M"]

# B = df[df.diagnosis == "B"]

# plt.title("Malignant vs Benign Tumor")
# plt.xlabel("Radius Mean")
# plt.ylabel("Texture Mean")
# plt.scatter(M.radius_mean, M.texture_mean, color = "red", label = "Malignant", alpha = 0.3)
# plt.scatter(B.radius_mean, B.texture_mean, color = "lime", label = "Benign", alpha = 0.3)
# plt.legend()
# plt.show()

# # df.diаgnоsis = [1 if i== "M" else 0 fоr i in df.diаgnоsis]
# x = df.drop(["diagnosis"], axis = 1)
# y = df.diagnosis.values

# Normalization:
# import numpy as np
# from numpy import *
# x = (x - nр.min(x)) / (nр.mаx(x) - nр.min(x))
# x = (x - min(x)) / (mаx(x) - min(x))

# # Test Train Split
# from sklearn.model_selection import train_test_split
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 42)

# # Sklearn Gaussian Naive Bayes Model
# def models(x_train,y_train):
#   from sklearn.naive_bayes import GaussianNB
#   nb = GaussianNB()
#   nb.fit(x_train, y_train)
#   # return nb
#   # Accuracy
#   print("Naive Bayes score: ",nb.score(x_test, y_test))
#   return nb

# model = models(x_train,y_train)

def modelss(X_train,Y_train):
  from sklearn.naive_bayes import GaussianNB
  gauss = GaussianNB()
  gauss.fit(X_train, Y_train)
  print('Gaussian Naive Bayes Training Accuracy:', gauss.score(X_train, Y_train))
  return gauss

model = modelss(X_train,Y_train)



"""Confusion Matrix"""

from sklearn.metrics import confusion_matrix
# for i in range(len(model)):
i=1
cm = confusion_matrix(Y_test, model.predict(X_test))

TN = cm[0][0]
TP = cm[1][1]
FN = cm[1][0]
FP = cm[0][1]

print(cm)
print('Model[{}] Testing Accuracy = "{}!"'.format(i,  (TP + TN) / (TP + TN + FN + FP)))
print()# Print a new line





"""# Decision Tree"""

#Decision Tree
#Using DecisionTreeClassifier
def decision(X_train,Y_train):
  from sklearn.tree import DecisionTreeClassifier
  tree = DecisionTreeClassifier(criterion = 'entropy', max_depth = 2)
  tree.fit(X_train, Y_train)
  print('Decision Tree Classifier Training Accuracy:', tree.score(X_train, Y_train))
  return tree
model = decision(X_train,Y_train)

def decision(X_train,Y_train):
  from sklearn.tree import DecisionTreeClassifier
  tree = DecisionTreeClassifier(criterion = 'entropy', max_depth = 7)
  tree.fit(X_train, Y_train)
  print('Decision Tree Classifier Training Accuracy:', tree.score(X_train, Y_train))
  return tree
model = decision(X_train,Y_train)

def decision(X_train,Y_train):
  from sklearn.tree import DecisionTreeClassifier
  tree = DecisionTreeClassifier(criterion = 'gini', max_depth = 2)
  tree.fit(X_train, Y_train)
  print('Decision Tree Classifier Training Accuracy:', tree.score(X_train, Y_train))
  return tree
model = decision(X_train,Y_train)

def decision(X_train,Y_train):
  from sklearn.tree import DecisionTreeClassifier
  tree = DecisionTreeClassifier(criterion = 'gini', max_depth = 7)
  tree.fit(X_train, Y_train)
  print('Decision Tree Classifier Training Accuracy:', tree.score(X_train, Y_train))
  return tree
model = decision(X_train,Y_train)



"""Confusion Matrix"""

from sklearn.metrics import confusion_matrix
# for i in range(len(model)):
i=2
cm = confusion_matrix(Y_test, model.predict(X_test))

TN = cm[0][0]
TP = cm[1][1]
FN = cm[1][0]
FP = cm[0][1]

print(cm)
print('Model[{}] Testing Accuracy = "{}!"'.format(i,  (TP + TN) / (TP + TN + FN + FP)))
print()# Print a new line





"""# Logistic Regression"""

def models(X_train,Y_train):
  #Using Logistic Regression
  from sklearn.linear_model import LogisticRegression
  log = LogisticRegression(random_state = 0)
  log.fit(X_train, Y_train)
  #print model accuracy on the training data.
  print('Logistic Regression Training Accuracy:', log.score(X_train, Y_train))
  return log
model = models(X_train,Y_train)



"""Confusion Matrix"""

from sklearn.metrics import confusion_matrix
# for i in range(len(model)):
i=3
cm = confusion_matrix(Y_test, model.predict(X_test))

TN = cm[0][0]
TP = cm[1][1]
FN = cm[1][0]
FP = cm[0][1]

print(cm)
print('Model[{}] Testing Accuracy = "{}!"'.format(i,  (TP + TN) / (TP + TN + FN + FP)))
print()# Print a new line





"""# SVM(Support Vector Machine)"""

def models(X_train,Y_train):
  #Using SVC linear
  from sklearn.svm import SVC
  svc_lin = SVC(kernel = 'linear', random_state = 0)
  svc_lin.fit(X_train, Y_train)
  print('Support Vector Machine (Linear Classifier) Training Accuracy:', svc_lin.score(X_train, Y_train))
  return svc_lin

model = models(X_train,Y_train)



"""Confusion Matrix"""

from sklearn.metrics import confusion_matrix
# for i in range(len(model)):
i=4
cm = confusion_matrix(Y_test, model.predict(X_test))

TN = cm[0][0]
TP = cm[1][1]
FN = cm[1][0]
FP = cm[0][1]

print(cm)
print('Model[{}] Testing Accuracy = "{}!"'.format(i,  (TP + TN) / (TP + TN + FN + FP)))
print()# Print a new line





"""# Comparing All"""

def models(X_train,Y_train):

  #Using KNeighborsClassifier
  from sklearn.neighbors import KNeighborsClassifier
  knn = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
  knn.fit(X_train, Y_train)

  #Using GaussianNB
  from sklearn.naive_bayes import GaussianNB
  gauss = GaussianNB()
  gauss.fit(X_train, Y_train)

  #Using DecisionTreeClassifier
  from sklearn.tree import DecisionTreeClassifier
  tree = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
  tree.fit(X_train, Y_train)

  #Using Logistic Regression
  from sklearn.linear_model import LogisticRegression
  log = LogisticRegression(random_state = 0)
  log.fit(X_train, Y_train)

  #Using SVC linear
  from sklearn.svm import SVC
  svc_lin = SVC(kernel = 'linear', random_state = 0)
  svc_lin.fit(X_train, Y_train)

  #print model accuracy on the training data.
  print('[2]K Nearest Neighbor Training Accuracy:', knn.score(X_train, Y_train))
  print('[4]Gaussian Naive Bayes Training Accuracy:', gauss.score(X_train, Y_train))
  print('[5]Decision Tree Classifier Training Accuracy:', tree.score(X_train, Y_train))
  print('[1]Logistic Regression Training Accuracy:', log.score(X_train, Y_train))
  print('[3]Support Vector Machine (Linear Classifier) Training Accuracy:', svc_lin.score(X_train, Y_train))



  return knn, gauss, tree, log, svc_lin

model = models(X_train,Y_train)

"""# Compairing Confusion Matrix"""

from sklearn.metrics import confusion_matrix
for i in range(len(model)):
  cm = confusion_matrix(Y_test, model[i].predict(X_test))

  TN = cm[0][0]
  TP = cm[1][1]
  FN = cm[1][0]
  FP = cm[0][1]

  print(cm)
  print('Model[{}] Testing Accuracy = "{}!"'.format(i,  (TP + TN) / (TP + TN + FN + FP)))
  print()# Print a new line

#Other ways to get the classification accuracy & other metrics

from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

for i in range(len(model)):
  print('Model ',i)
  #Check precision, recall, f1-score
  print( classification_report(Y_test, model[i].predict(X_test)) )
  #Another way to get the models accuracy on the test data
  print( accuracy_score(Y_test, model[i].predict(X_test)))
  print()#Print a new line

#Print Prediction of Decision Tree model
pred = model[2].predict(X_test)
print(pred)

#Print a space
print()

#Print the actual values
print(Y_test)