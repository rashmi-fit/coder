#how classification algortihm works
import pandas as pd
import matplotlib.pyplot as plt

fruits = pd.read_table('/Users/rmn7591/Documents/Repositories/coder/Algorithm/fruits_data.txt')
print(fruits.head())

print(fruits.shape)
print(fruits['fruit_name'].unique())
print(fruits.groupby('fruit_name').size())

import seaborn as sns
sns.countplot(fruits['fruit_name'],label="Count")
plt.show()

fruits.drop('fruit_label', axis=1).plot(kind='box', subplots=True,layout=(2,2),sharex=False,figsize=(9,9), title='Box Plot for each input variable')
plt.savefig('fruits_box')
plt.show()

#plotting
features_names=['mass','width','height','color_score']
x=fruits[features_names]
y=fruits[features_names]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0)

from sklearn.preprocessing import MinMaxScaler
scaler= MinMaxScaler()
x_train-scaler.fir_transform(x_train)
x_test=scaler.transform(x_test)

#Logistic regression

from sklearn.linear_model import LogisticRegression
logreg=LogisticRegression()
logreg.fit(x_train,y_train)
print('Accuracy of logistic regression classifier on training set :{:.2f}'.format(logreg.score(x_train,y_train)))
print('Accuracy of logistic regression classifier on test set :{:.2f}'.format(logreg.score(x_test,y_test)))

#Decision tree

from sklearn.tree import DecisionTreeClassifier
clf=DecisionTreeClassifier().fit(x_train,y_train)
print('Accuracy of Decision Tree classifier on training set :{:.2f}'.format(clf.score(x_train,y_train)))
print('Accuracy of Decision Tree classifier on testing set :{:.2f}'.format(clf.score(x_test,y_test)))

#KNN Classifier
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier()
knn.fit(x_train,y_train)
print('Accuracy of K-NN classifier on training set :{:.2f}'.format(knn.score(x_train,y_train)))
print('Accuracy of K-NN classifier on testing set :{:.2f}'.format(knn.score(x_test,y_test)))

#NaiveBayes

from sklearn.neighbors import GaussianNB
gnb=GaussianNB()
gnb.fit|(x_train,y_train)
print('Accuracy of GNB classifier on training set :{:.2f}'.format(gnb.score(x_train,y_train)))
print('Accuracy of GNB classifier on testing set :{:.2f}'.format(gnb.score(x_train,y_train)))

#Support vector machine classifier

from sklearn.svm import SVC
svm=SVC()
svm.fit(x_train,y_train)
print('Accuracy of SVM classifier on training set :{:.2f}'.format(svm.score(x_train,y_train)))
print('Accuracy of SVM classifier on testing set :{:.2f}'.format(svm.score(x_train,y_train)))

#confusion matrix for knn classifier

gamma='auto'
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
pred=knn.predict(x_test)
print(confusion_matrix(y_test,pred))
print(classification_report(y_test,pred))













