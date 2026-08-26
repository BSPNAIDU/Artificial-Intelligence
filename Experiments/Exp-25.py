# Exp-25: Feed Forward Neural Network

from sklearn.neural_network import MLPClassifier

# XOR dataset
X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

y = [0, 1, 1, 0]

# Create Feed Forward Neural Network
model = MLPClassifier(
    hidden_layer_sizes=(4,),
    activation="relu",
    solver="lbfgs",
    max_iter=1000,
    random_state=42
)

# Train the model
model.fit(X, y)

print("Feed Forward Neural Network trained successfully.\n")

# Test predictions
predictions = model.predict(X)

print("Input\t\tExpected\tPredicted")

for i in range(len(X)):
    print(
        X[i],
        "\t\t",
        y[i],
        "\t\t",
        predictions[i]
    )

# User input
a = int(input("\nEnter first input (0 or 1): "))
b = int(input("Enter second input (0 or 1): "))

prediction = model.predict([[a, b]])

print("Predicted Output:", prediction[0])