import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np

iris = load_iris()
X,y = iris.data , iris.target

X_train , X_test , y_train , y_test = train_test_split(X,y , test_size =0.25 ,random_state=42)

model = RandomForestClassifier()
model.fit(X_train , y_train)

print(model.score(X_test,y_test))
print(iris.target_names)
#input_data =np.array([[1,2.4 ,2 ,1.2]])
#print(model.predict(input_data))


with open('model.pkl','wb') as file:
    pickle.dump(model , file)