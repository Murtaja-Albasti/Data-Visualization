import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

Spotify_data = pd.read_csv("./spotify.csv" , index_col='Date',parse_dates=True)

#plot the data

plt.figure(figsize=(14,6))
plt.title("the heighest songs ever. ")

sns.lineplot(data=Spotify_data['Shape of You'],label = "shape of you")
sns.lineplot(data=Spotify_data['Despacito'], label = "Despacito")

plt.show()