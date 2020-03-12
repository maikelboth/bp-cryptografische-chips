#!/usr/bin/python3

import matplotlib.pyplot as plt

data1 = range(10, 0, -1)
data2 = range(10)
data3 = [5] * 10

plt.plot(data1, label="Demo")
plt.plot(data2)
plt.plot(data3,)

plt.ylabel('Wallet [ € ]')
plt.legend(loc='lower left')
plt.show()
