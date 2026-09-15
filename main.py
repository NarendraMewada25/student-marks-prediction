import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Load dataset
data = pd.read_csv("data.csv")

# Input features
X = data[["StudyHours", "PreviousMarks"]]

# Target value
y = data["FinalMarks"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)

# Calculate model accuracy
accuracy = r2_score(y_test, y_pred)

print("\n======================================")
print("      STUDENT MARKS PREDICTION")
print("======================================")

print("\nModel R2 Score:", round(accuracy, 2))
print("Model Accuracy:", round(accuracy * 100, 2), "%")

# Get student details
study_hours = float(input("\nEnter study hours: "))
previous_marks = float(input("Enter previous marks: "))

# Predict final marks
prediction = model.predict([[study_hours, previous_marks]])

print("\n--------------------------------------")
print("Predicted Final Marks:", round(prediction[0], 2))
print("--------------------------------------")
print("Prediction completed successfully!")