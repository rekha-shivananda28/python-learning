from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

X=[[1000],[1500],[2000],[2500],[3000],[3500]]
y=[20,30,40,50,60,70]

X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.33,random_state=42
)
model=LinearRegression()
model.fit(X_train,y_train)

predictions=model.predict(X_test)

error=mean_absolute_error(y_test,predictions)

print("Actual prices:",y_test)
print("Predicted prices:",predictions)
print("Mean Absolute Error:",error)

new_house=model.predict([[1800]])
print("Predicted price for 1800 sq.ft:",new_house[0],"lakh")