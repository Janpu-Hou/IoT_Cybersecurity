import joblib
# Example of loading the datasets back
X_train=joblib.load('X_train.joblib')
X_test=joblib.load('X_test.joblib')
y_train=joblib.load('y_train.joblib')
y_test=joblib.load('y_test.joblib')

print("Datasets loaded successfully!")