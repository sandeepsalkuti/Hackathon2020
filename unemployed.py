#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python37-32\python.exe

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

import warnings
import pickle
warnings.filterwarnings("ignore")

data = pd.read_csv("edited.csv")
data = np.array(data)

X = data[1:, 1:-1]
y = data[1:, -1]
y = y.astype('int')
X = X.astype('int')
# print(X,y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
#log_reg = LogisticRegression()
clf = DecisionTreeClassifier()


#log_reg.fit(X_train, y_train)
dtree_model = clf.fit(X_train, y_train)

inputt=[int(x) for x in "276 183 954".split(' ')]
final=[np.array(inputt)]


#b = log_reg.predict_proba(final)
b = dtree_model.predict(final)

pickle.dump(log_reg,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))


