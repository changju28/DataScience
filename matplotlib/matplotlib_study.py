import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/broadcast.csv', index_col=0)

# print(df)
plt.plot(df[['KBS', 'JTBC']])
plt.savefig('exam.png')
plt.show()

