import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

Iris_file = './iris.csv'
Iris_data = pd.read_csv(Iris_file,index_col='Id')

plt.figure(figsize=(14,6))

sns.histplot(data=Iris_data, x='Sepal Width (cm)' , hue='Species')

plt.show()