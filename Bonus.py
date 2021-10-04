# Enable matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from sklearn.linear_model import LinearRegression
import seaborn as sns

# Predict a point in the future.
sales = pd.read_csv('SalesOfShampoo.csv')
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(sales.Year.values.reshape(-1,1), sales.SalesinMillions.values.reshape(-1,1), random_state=1)
lr = LinearRegression()
lr.fit(X=X_train, y=y_train)
plt.scatter(X_train, y_train, color = 'blue')
plt.plot(X_train, lr.predict(X_train), color = 'black')
plt.show()

# SciPy stats module linregress function to calculate slope and intercept
linear_regression = stats.linregress(x=sales.Year, y=sales.SalesinMillions)
print(f'Slope - {linear_regression.slope}')
print(f'Intercept - {linear_regression.intercept}')
pred2021 = linear_regression.slope*2021 +linear_regression.intercept
print(f'Prediction for 2021 Sales - {pred2021}')

#Chart the data with the best-fit line
sns.set_style('whitegrid')
axes = sns.regplot(x=sales.Year, y=sales.SalesinMillions)
plt.show()








