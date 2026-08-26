# Exp-24: Decision Tree

from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

# Dataset
# [Weather, Temperature]
# Weather: 0 = Sunny, 1 = Rainy
# Temperature: 0 = Cold, 1 = Hot

X = [
    [0, 1],
    [0, 1],
    [1, 0],
    [1, 1],
    [0, 0],
    [1, 0]
]

# 0 = No, 1 = Yes
y = [1, 1, 0, 0, 0, 0]

model = DecisionTreeClassifier(
    criterion="entropy",
    random_state=42
)

model.fit(X, y)

print("Decision Tree Model created successfully.")

# Prediction
weather = int(input(
    "Enter weather (0=Sunny, 1=Rainy): "
))

temperature = int(input(
    "Enter temperature (0=Cold, 1=Hot): "
))

prediction = model.predict([[weather, temperature]])

if prediction[0] == 1:
    print("Prediction: Yes")
else:
    print("Prediction: No")

# Display tree rules
print("\nDecision Tree:")
print(tree.export_text(model))