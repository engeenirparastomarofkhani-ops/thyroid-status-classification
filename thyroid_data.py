import pandas as pd
from sklearn.tree import DecisionTreeClassifier

columns = ['Thyroid_status', 'TSH', 'FT4', 'FT3']
DF = pd.DataFrame(columns=columns)

for x in range(15):
    STD = {
        "Thyroid_status": input("plz enter thyroid status: "),
        "TSH": float(input("plz enter TSH value: ")),
        "FT4": float(input("plz enter FT4 value: ")),
        "FT3": float(input("plz enter FT3 value: "))
    }
    
    DF.loc[len(DF)] = STD

print(DF)

DF.to_csv('thyroid_data.csv', index=False)




