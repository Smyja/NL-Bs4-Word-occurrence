import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from datetime import date

csv = pd.read_csv("/storage/emulated/0/PythonCodex/fitle.csv")
x1, x2 = csv.values.T
dates = [date(2019, 4, x).strftime("%d %B") for x in range(1, len(x1) + 1)]

frame = pd.DataFrame({'Afonja': x1, 'pigs': x2}, index=dates)
print(frame)
frame.plot(kind="bar")


#plt.show()




'''
plt.scatter(x1, y, label='Afonja')
plt.scatter(x2, y, label='pigs')
plt.plot(x, y)

'''

plt.xlabel('Slurs')
plt.ylabel('Occurrences')
plt.legend()
plt.show()
