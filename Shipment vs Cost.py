import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('SCMS_Delivery_History_Dataset.csv')

df["Freight Cost (USD)"] = pd.to_numeric(df["Freight Cost (USD)"], errors="coerce")
df = df.dropna(subset=["Freight Cost (USD)"])

df.groupby("Shipment Mode")["Freight Cost (USD)"].mean().sort_values().plot(kind="bar")

plt.title("Cost per Shipment Mode")
plt.xlabel("Shipment Mode")
plt.ylabel("Average Freight Cost (USD)")

plt.tight_layout()
plt.show()