#first we need to install pandas
#pip install pandas
import pandas as pd

inmuebles = pd.read_csv('inmuebles_bogota.csv')
print(inmuebles.head())