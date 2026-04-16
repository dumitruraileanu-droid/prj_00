from Verspätungen import delayed
import pandas as pd
import matplotlib.pyplot as plt


print(delayed.columns)
shipment = delayed['Shipment Mode'].value_counts()
fig = plt.figure()
ax = shipment.plot(kind='bar')
plt.xticks(rotation=0)
plt.title("Verspätung pro Shipment Mode")
plt.xlabel('Shipment Mode')
plt.ylabel('Anzahl der verspäteten Sendungen')

for i, value in enumerate(shipment):
    ax.text(i, value, str(value), ha='center', va='bottom')

plt.tight_layout()
plt.show()