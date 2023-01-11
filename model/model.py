from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd 
from sklearn.tree import DecisionTreeClassifier 
from sklearn import tree

#data= pd.read_csv("C:\\Users\\User\\OneDrive\\Documents\\sem 7\\FYP 2\\gui\\initialGUI\\prediction\\ThisDataset.csv")
data= pd.read_csv("C:\\Users\\User\\OneDrive\\Documents\\PrototypeFYP\\post-strokeGUI\\model\\Dataset.csv")
X = data.iloc[:, [12, 11,10,9]].values
y = data.iloc[:, 13].values

X_train, X_test, y_train, y_test = train_test_split(
    X,y, test_size=0.2
)

clf = DecisionTreeClassifier(random_state=1234)
model=clf.fit(X_train, y_train)

text_representation = tree.export_text(clf)
print(text_representation)

predictions= clf.predict(X_test)

def accuracy(y_test, y_pred):
    return np.sum(y_test ==y_pred)/len(y_test)

acc = accuracy(y_test, predictions)
print(acc)