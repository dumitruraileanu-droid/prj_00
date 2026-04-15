import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('SCMS_Delivery_History_Dataset.csv')

shipment=df['Shipment Mode'].value_counts()


fig = plt.figure()

plt.bar(shipment.index, shipment.values)
plt.show()