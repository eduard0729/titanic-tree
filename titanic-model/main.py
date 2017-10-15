from sklearn.datasets import load_iris
from sklearn import tree
from sklearn import metrics
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')

iris = load_iris()
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

train.shape #Number of col & row
test.shape

#train.describe()
#test.describe()

#train.info() 
#test.info()

# Find missing values in respective column
train.isnull().sum()
test.isnull().sum()

train_len= len(train)
dataset = pd.concat(objs= [train,test],axis=0) #index(drop=True)
#Data Exploration
dataset.head()

#Fill empty and NaN values with NaN
dataset =dataset.fillna(np.nan)

dataset.isnull().sum()

#Replacing missing value
dataset.Embarked.value_counts()
dataset['Embarked'] = dataset['Embarked'].fillna('S')

dataset['Age']=dataset.Age.fillna(dataset.Age.mean())

dataset.Fare=dataset.Fare.fillna(dataset.Fare.mean())

dataset.drop(['Name','Cabin','Ticket'],inplace =True,axis=1)

#Data set 
dataset.hist(figsize=(9,9),grid=1)
dataset.boxplot()

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
for column in ['Sex','Embarked']:
    le.fit(list(dataset[column].values))
    dataset[column]=le.transform(dataset[column])
    

x_train1=dataset.iloc[:891,:8]
y_train1 =dataset.iloc[:891,8:]
x_test1=dataset.iloc[891:,:8]
y_test1=dataset.iloc[891:,8:]


clf = tree.DecisionTreeClassifier()

clf = clf.fit(x_train1, y_train1)
import graphviz 

dot_data = tree.export_graphviz(clf, out_file=None, 
                         feature_names=['Age', 'Embarked', 'Fare', 'Parch', 'PassengerId', 'Pclass','Sex', 'SibSp'],  
                         class_names=['Survived', 'Dead'],  
                         filled=True, rounded=True,  
                         special_characters=True)  

graph = graphviz.Source(dot_data) 
graph.render("titanic") 

y_pred= clf.predict(x_test1)
le.fit(y_pred)
y_pred = le.transform(y_pred)
print y_pred
print y_test1

submit = pd.DataFrame({'PassengerId':test['PassengerId'],'Survived':y_pred})
submit.to_csv('titanic.csv',index=False)


from sklearn.externals import joblib
joblib.dump(clf, 'titanic.pkl') 


