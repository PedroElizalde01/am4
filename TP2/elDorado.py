import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

1.
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
columns = ["latitud", "longitud"]
file = open('./TP2/ship_geo_position.csv')
df = pd.read_csv(file, usecols=columns)
plt.plot(df.latitud, df.longitud)
plt.show()

#2.
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
columns = ["latitud", "longitud"]
file = open('./TP2/seaquake_geo_position.csv')
df = pd.read_csv(file, usecols=columns)
plt.plot(df.latitud, df.longitud)
plt.show()

#3.


#4.

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
columns = ["latitud", "longitud"]
file = open('./TP2/ship_pos.csv')
df = pd.read_csv(file, usecols=columns)
plt.plot(df.latitud, df.longitud)
plt.show()