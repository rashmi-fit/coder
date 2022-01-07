# Forecast maximum temperature using linear regression (relationship betweeen max and min temp)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

dataset =  pd.read_csv('city_temperature.csv') #  put the path of the file here
print(dataset.shape)
print(dataset.describe())

# Ploting and manually trying to make relationship between x and y
dataset.plot(x='MiniTemp', y='MaxTemp', style=0)
plt.title('MiniTemp Vs MaxTemp')
plt.xlabel('MiniTemp')
plt.ylabel('MaxTemp')
plt.show()

# It will show average maximum temperature that we have EDA
plt.figure(figsize=(15,10))
plt.tight_layout()
seabornInstance.displot(dataset['MaxTemp'])
plt.show()

# Data splicing
x=dataset['MiniTemp'].values.reshape(-1,1)
y=dataset['MaxTemp'].values.reshape(-1,1)

x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2,random_state=0)
regressor=LinearRegression()
regressor.fit(x_train,y_train) #traning the algorithm

# To retrieve the intercept
print('Intercept',regressor.intercept_)
print('Coefficient',regressor.coef_) #B0
y_pred=regressor.predict(x_test)

df=pd.DataFrame({'Actual' : y_test.flatten(), 'Predicted'  : y_pred.flatten()})
print(df)

df1=df.head(25)
df1.plot(kind='bar',figsize=(16,10))
plt.grid(which='major',linestyle='-', linewiddth='0.5', color='green')
plt.grid(which='major',linestyle=':', linewiddth='0.5', color='black')
plt.show()

# drawing a straight line plot
plt.scatter(x_test,y_test,color='grey')
plt.plot(x_test,y_pred,color='red',linewidth=2)
plt.sho()

# Evaluate the performance
print('Mean Absolute Error:' ,metrics.mean_absolute_error(y_test,y_pred))
print('Mean squared Error:' ,metrics.mean_squared_error(y_test,y_pred))
print('Root Mean squared Error:' , np.sqrt(metrics.mean_squared_error(y_test,y_pred)))


