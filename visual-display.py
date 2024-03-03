import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 表示console控制台下 读取
data = pd.read_csv('.//name_score.csv')

fig = plt.figure(figsize=(5,6))
fig.subplots_adjust(hspace=0.3)
ax1 = fig.add_subplot(211)
sns.lineplot(data=data,x='math',y='physical',hue='gender',errorbar=('ci', 0))
ax1.legend(loc='upper left',frameon=False)
ax2 = fig.add_subplot(212)
sns.lineplot(data=data,x='math',y='chemistry',errorbar=('ci', 0))