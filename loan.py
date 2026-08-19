import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

# Create dataset
data = {
    'Age': [25, 35, 45, 28, 50, 30, 40, 23, 55, 38],
    'Income': [30000, 60000, 80000, 25000, 90000,
               45000, 70000, 20000, 100000, 65000],
    'CreditScore': [650, 720, 780, 600, 800,
                    700, 750, 580, 820, 730],
    'LoanAmount': [500000, 1000000, 1500000, 400000, 1200000,
                   800000, 1000000, 300000, 1800000, 900000],
    'EmploymentYears': [2, 8, 15, 1, 20,
                        5, 10, 1, 25, 7],
    'LoanStatus': ['Rejected', 'Sanctioned', 'Sanctioned',
                   'Rejected', 'Sanctioned', 'Sanctioned',
                   'Sanctioned', 'Rejected', 'Sanctioned',
                   'Sanctioned']
}

df = pd.DataFrame(data)

# Input features
X = df[['Age', 'Income', 'CreditScore',
        'LoanAmount', 'EmploymentYears']]

# Target
y = df['LoanStatus']

# Create Decision Tree
model = DecisionTreeClassifier(
    criterion='entropy',
    max_depth=3,
    random_state=42
)

# Train model
model.fit(X, y)

# Predict a new customer's loan status
new_customer = [[32, 55000, 710, 700000, 6]]

prediction = model.predict(new_customer)

print("Predicted Loan Status:", prediction[0])

# Display tree
plt.figure(figsize=(15, 8))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=model.classes_,
    filled=True
)

plt.show()