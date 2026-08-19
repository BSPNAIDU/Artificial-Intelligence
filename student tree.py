import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Create dataset
data = {
    'Attendance': [85,60,90,55,75,50,82,65,92,78],
    'InternalMarks': [78,45,88,40,65,35,72,50,90,70],
    'Assignment': [90,50,95,45,70,40,80,55,95,75],
    'StudyHours': [4,2,5,1,3,1,4,2,6,3],
    'Result': ['Pass','Fail','Pass','Fail','Pass',
               'Fail','Pass','Fail','Pass','Pass']
}

df = pd.DataFrame(data)

# Input features
X = df[['Attendance', 'InternalMarks',
        'Assignment', 'StudyHours']]

# Target
y = df['Result']

# Create Decision Tree
model = DecisionTreeClassifier(
    criterion='entropy',
    max_depth=3,
    random_state=42
)

# Train model
model.fit(X, y)

# Predict a new student's result
new_student = [[80, 70, 75, 3]]

prediction = model.predict(new_student)

print("Predicted Result:", prediction[0])

# Display tree
plt.figure(figsize=(12, 7))
plot_tree(
    model,
    feature_names=X.columns,
    class_names=model.classes_,
    filled=True
)
plt.show()