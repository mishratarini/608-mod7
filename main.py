# Enable matplotlib
import matplotlib as matplotlib
import pandas as pd


# Plot Celsius vs Farenhiet
c = lambda f: 5/9 * (f - 32)
temps = [(f, c(f)) for f in range (0, 101, 10)]
temps_df = pd.DataFrame(temps, columns=['Fahrenheit', 'Celsius'])
axes = temps_df.plot(x='Fahrenheit', y='Celsius', style='.-')
y_label = axes.set_ylabel('Celsius')
#matplotlib.pyplot.show()

# load and clean NY City January high temperature
nyc = pd.read_csv('ave_hi_nyc_jan_1895-2018.csv')
print(nyc.head())
print(nyc.tail())
nyc.columns = ['Date', 'Temperature', 'Anomaly']
nyc.Date = nyc.Date.floordiv(100)
print(nyc.head(3))
pd.set_option('Precision',2)
print(nyc.Temperature.describe())

#Predict Jan 2021 temperature
from scipy import stats
linear_regression = stats.linregress(x=Date, y=nyc.Temperature)
print(f'Slope - {linear_regression.slope}')
print(f'Intercept - {linear_regression.intercept}')
print(f'Prediction for Jan 2021 Max Temperatrure- {linear_regression.slope*2021 +linear_regression.intercept}')




