import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

Flight_file = "./flight_delays.csv"
Flight_data = pd.read_csv(Flight_file, index_col='Month')
# plotting
plt.figure(figsize=(13, 6))
plt.title("Average arrival delay for NK airlines")
sns.barplot(x=Flight_data.index, y=Flight_data['NK'])
plt.xlabel("airlines")
plt.show()
