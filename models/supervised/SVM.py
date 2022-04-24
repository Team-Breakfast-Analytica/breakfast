from sklearn.svm import SVR
#Build and Run a Support Vector Machine for All Features

svm = SVR(kernel="linear")
svm.fit(X_train,y_train)

training_preds_svm = svm.predict(X_train)
val_preds_svm = svm.predict(X_test)

print("\nTraining Mean Squared Error:", round(mean_squared_error(y_train, training_preds_svm),4))
print("Validation Mean Squared Error:", round(mean_squared_error(y_test, val_preds_svm),4))
print("\nTraining r2 score:", round(r2_score(y_train, training_preds_svm),4))
print("Validation r2 score:", round(r2_score(y_test, val_preds_svm),4))

#Build and Run a SVM for Listings Features Without POI
svm.fit(X2_train,y2_train)

training_preds_svm2 = svm.predict(X2_train)
val_preds_svm2 = svm.predict(X2_test)

print("\nTraining Mean Squared Error:", round(mean_squared_error(y2_train, training_preds_svm2),4))
print("Validation Mean Squared Error:", round(mean_squared_error(y2_test, val_preds_svm2),4))
print("\nTraining r2 score:", round(r2_score(y2_train, training_preds_svm2),4))
print("Validation r2 score:", round(r2_score(y2_test, val_preds_svm2),4))

#Build and Run a SVM for POI Features
svm.fit(X3_train,y3_train)

training_preds_svm3 = svm.predict(X3_train)
val_preds_svm3 = svm.predict(X3_test)

print("\nTraining Mean Squared Error:", round(mean_squared_error(y3_train, training_preds_svm3),4))
print("Validation Mean Squared Error:", round(mean_squared_error(y3_test, val_preds_svm3),4))
print("\nTraining r2 score:", round(r2_score(y3_train, training_preds_svm3),4))
print("Validation r2 score:", round(r2_score(y3_test, val_preds_svm3),4))