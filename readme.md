# Student Marks Prediction

## 1. Project Description

Student Marks Prediction is a simple Machine Learning project that predicts a student's final marks based on their study hours and previous marks.

The project uses the Linear Regression algorithm to learn the relationship between study hours, previous marks, and final marks.

## 2. Features

* Reads student data from a CSV file
* Trains a Linear Regression model
* Evaluates the model using the R² score
* Takes study hours and previous marks as input
* Predicts the student's final marks
* Runs completely from the command line

## 3. Technologies Used

* Python
* Pandas
* Scikit-learn
* Linear Regression

## 4. Project Structure

```text
student-marks-prediction/
│
├── main.py
├── data.csv
├── requirements.txt
└── README.md
```

## 5. Requirements

Make sure Python is installed on your computer.

The required Python libraries are listed in `requirements.txt`.

## 6. Installation

Open the terminal inside the project folder and run:

```bash
pip install -r requirements.txt
```

If the above command does not work, use:

```bash
python -m pip install -r requirements.txt
```

## 7. How to Run

Run the following command:

```bash
python main.py
```

The program will ask for:

1. Study hours
2. Previous marks

Example:

```text
======================================
      STUDENT MARKS PREDICTION
======================================

Model R2 Score: 0.99
Model Accuracy: 99.12 %

Enter study hours: 6
Enter previous marks: 75

--------------------------------------
Predicted Final Marks: 77.18
--------------------------------------
Prediction completed successfully!
```

The exact R² score and predicted marks may vary depending on the dataset.

## 8. Machine Learning Method

The project uses **Linear Regression**.

The input feature
