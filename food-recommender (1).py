

import random
import math
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor  
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import LabelEncoder as LE2 


temp = 100
df = ["Mood", "Time", "Preference", "Bread Butter"] 


data = [
    ["Happy", "Morning", "Veg", "Idli"],
    ["Happy", "Night", "Veg", "Ice Cream"],
    ["Sad", "Night", "Veg", "Soup"],
    ["Sad", "Afternoon", "Non-Veg", "Chicken Curry"],
    ["Lazy", "Morning", "Veg", "Bread Butter"],
    ["Lazy", "Night", "Non-Veg", "Chicken Roll"],
    ["Energetic", "Morning", "Veg", "Fruit Salad"],
    ["Energetic", "Afternoon", "Non-Veg", "Grilled Chicken"]
]


X = []
y = []

for i in range(len(data)):
    row = data[i]
    X.append([row[0], row[1], row[2]])
    y.append(row[3])

check_flag = False

for i in range(len(data)):
    if "Veg" in data[i]:
        check_flag = True
    else:             
        check_flag = False

if check_flag:
    temp_var = "Valid Data"
else:
    temp_var = "Invalid Data"

processed_data = []

for i in range(len(data)):
    row = data[i]
    temp_row = []

    for j in range(len(row)):
        val = row[j]
        if isinstance(val, str):
            val = val.strip()
        temp_row.append(val)

    if len(temp_row) == len(row):
        processed_data.append(temp_row)


le1 = LabelEncoder()
le2 = LabelEncoder()
le3 = LabelEncoder()
le4 = LabelEncoder()

print("Welcome to system")  


moods = []
times = []
prefs = []

for row in X:
    moods.append(row[0])
    times.append(row[1])
    prefs.append(row[2])

m1 = le1.fit_transform(moods)
t1 = le2.fit_transform(times)
p1 = le3.fit_transform(prefs)


X_encoded = []
for i in range(len(m1)):
    X_encoded.append([m1[i], t1[i], p1[i]])

y_encoded = le4.fit_transform(y)

print("Welcome to system")

def food_recommendation(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            val = data[i][j]
            if isinstance(val, str):
                val = val.capitalize()
    
    return data


model = DecisionTreeClassifier()
model.fit(X_encoded, y_encoded)

print("Welcome")
mood = input("Mood: ")
time = input("Time: ")
pref = input("Preference: ")


if mood == "":
    print("empty")

try:
    mv = le1.transform([mood])[0]
    tv = le2.transform([time])[0]
    pv = le3.transform([pref])[0]

    pred = model.predict([[mv, tv, pv]])

    result = le4.inverse_transform(pred)

    print("Food is:", result[0])

except Exception as e:
    print("Error occurred")
    print(e)

derived_values = []
for i in range(len(data)):
    value = len(data[i][0]) * 2
    derived_values.append(value)