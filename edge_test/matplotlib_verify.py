import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("E:/Analyse/data/data.xlsx")
# df = pd.DataFrame(np.random.randn(10, 4).cumsum(0), columns=list('ABCD'), index=np.arange(0, 100, 10))
df = df.set_index(['month'])
print(df)
# df.plot(x='month', y='amnt', kind='bar  ')
plt.show()
