import joblib
# Example of loading the datasets back
loaded_X_train=joblib.load('X_train.joblib')
loaded_X_test=joblib.load('X_test.joblib')
loaded_y_train=joblib.load('y_train.joblib')
loaded_y_test=joblib.load('y_test.joblib')

print("Datasets loaded successfully!")