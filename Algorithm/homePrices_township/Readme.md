Problem statement
- Predict home prices using multivariate linear regression 
- Data set is from one of the references

Analysis 
- In python (using sklearn linear_model). Home prices are dependent on 3 independent variables: area, bedrooms and age.
- Pandas dataframe is used to fill missing values first and then use that dataset to train a multivariate regression model.
- Math function has been used to get the median of bedrooms as one of them is null
- Using fillna i have filled all the NAN values with its median
- Here 'area','bedrooms','age' are dependent variable and price is independent variable
- As per the linear algebra y=m1x1+m2x2+m3x3+b
