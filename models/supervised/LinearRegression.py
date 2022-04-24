#Build and Run a Linear Regression Model for All Features.
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X_train, y_train)
lr.predict(X_test)

training_preds_lr = lr.predict(X_train)
val_preds_lr = lr.predict(X_test)


print("\nTraining Mean Squared Error:", round(mean_squared_error(y_train, training_preds_lr),4))
print("Validation Mean Squared Error:", round(mean_squared_error(y_test, val_preds_lr),4))
print("\nTraining r2 score:", round(r2_score(y_train, training_preds_lr),4))
print("Validation r2 score:", round(r2_score(y_test, val_preds_lr),4))

#Build and Run a Linear Regression Model for Listings Features Without POI

lr.fit(X2_train, y2_train)
lr.predict(X2_test)

training_preds_lr2 = lr.predict(X2_train)
val_preds_lr2 = lr.predict(X2_test)


print("\nTraining Mean Squared Error:", round(mean_squared_error(y2_train, training_preds_lr2),4))
print("Validation Mean Squared Error:", round(mean_squared_error(y2_test, val_preds_lr2),4))
print("\nTraining r2 score:", round(r2_score(y2_train, training_preds_lr2),4))
print("Validation r2 score:", round(r2_score(y2_test, val_preds_lr2),4))


#Build and Run a Linear Regression Model for POI Features

lr.fit(X3_train, y3_train)
lr.predict(X3_test)

training_preds_lr3 = lr.predict(X3_train)
val_preds_lr3 = lr.predict(X3_test)


print("\nTraining Mean Squared Error:", round(mean_squared_error(y3_train, training_preds_lr3),4))
print("Validation Mean Squared Error:", round(mean_squared_error(y3_test, val_preds_lr3),4))
print("\nTraining r2 score:", round(r2_score(y3_train, training_preds_lr3),4))
print("Validation r2 score:", round(r2_score(y3_test, val_preds_lr3),4))