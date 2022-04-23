#Build and Run the XGBoost Neural Network with the Grouped Dataframe.

# Split into train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

# Fit the model
xgb_reg = xgb.XGBRegressor()
xgb_reg.fit(X_train, y_train)
training_preds_xgb_reg = xgb_reg.predict(X_train)
val_preds_xgb_reg = xgb_reg.predict(X_test)

# Print results
print("\nTraining Mean Squared Error:", round(mean_squared_error(y_train, training_preds_xgb_reg),4))
print("Validation Mean Squared Error:", round(mean_squared_error(y_test, val_preds_xgb_reg),4))
print("\nTraining r2 score:", round(r2_score(y_train, training_preds_xgb_reg),4))
print("Validation r2 score:", round(r2_score(y_test, val_preds_xgb_reg),4))


# View in dataframe

print("XGBoost Feature Weights for All Features")
fw_xgb_reg = pd.DataFrame(xgb_reg.feature_importances_, columns=['weight'], index=X_train.columns)
fw_xgb_reg.sort_values('weight', ascending=False, inplace=True)
fw_xgb_reg