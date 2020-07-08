from matplotlib import pyplot as plt
import pandas as pd

datafile=pd.read_excel("AVAILABILITY_WATER_NEAR_LATERINE.xlsx", "ALOCATION OF FUND FOR DRINKING ")

plt.plot(datafile['States/UTs'], datafile['2018-19 (BE stage) - Allocation'])

plt.xlabel('States/UTs')
plt.ylabel('Fund allocated in rupees')
plt.title('Allocation of fund for drinking water')
plt.show()

