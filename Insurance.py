import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

insurance_file = "./insurance.csv"

insurance_data = pd.read_csv(insurance_file)
print(insurance_data.columns)

#plot
plt.figure(figsize=(13,6))
plt.title("insurance scatter data")
sns.scatterplot(x=insurance_data['bmi'],y=insurance_data['charges'],hue=insurance_data["smoker"])

plt.show()