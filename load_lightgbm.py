# Load the model from disk
loaded_model = joblib.load(model_filename)
print(f"Model loaded from {model_filename}")

# You can now use the loaded_model for predictions
# For example, to make predictions on X_test:
loaded_predictions = loaded_model.predict(X_test)

# And verify its performance (optional)
print("\nVerification of Loaded Model Performance:")
accuracy_loaded = accuracy_score(y_test, loaded_predictions)
print(f"Accuracy (Loaded Model): {accuracy_loaded:.4f}")
print("\nClassification Report (Loaded Model):")
print(classification_report(y_test, loaded_predictions))