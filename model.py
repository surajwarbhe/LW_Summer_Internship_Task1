import pandas as pd
import joblib

db = pd.read_csv('Salary_Data.csv')
x = db['YearsExperience'].values.reshape(1,-1)
y = db['Salary']

from sklearn.linear_model import LinearRegression
model = LinearRegression()
moodel.fit(x,y)
joblib.dump(model,'salary.pk1')
