from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split

Data = pd.read_csv('thyroid_data.csv')

X=Data[['TSH', 'FT4', 'FT3']] #fiturers
Y=Data['Thyroid_status'] #labels

x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

model = DecisionTreeClassifier()
model.fit(x_train, y_train)

accuracy = model.score(x_test, y_test)
print(f"Model accuracy: {accuracy*100:.2f}%")

X_new = pd.DataFrame(
    [[1.2, 1.1, 3.0]],
    columns=['TSH', 'FT4', 'FT3']
)

print(model.predict(X_new))
