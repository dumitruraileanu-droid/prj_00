import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('SCMS_Delivery_History_Dataset.csv')

# Conversie la numeric
df["Freight Cost (USD)"] = pd.to_numeric(df["Freight Cost (USD)"], errors="coerce")

# Elimină valori NaN (dacă există)
df = df.dropna(subset=["Freight Cost (USD)"])

df.groupby("Shipment Mode")["Freight Cost (USD)"].mean().plot(kind="barh")

plt.xlabel("Shipment Mode")
plt.ylabel("Average Cost")
plt.title("Price per Shipment Mode")
plt.tight_layout()
plt.show()