import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('SCMS_Delivery_History_Dataset.csv')

#df["Freight Cost (USD)"] = df["Freight Cost (USD)"].astype(str) \
 #   .str.replace(",", "") \
  #  .str.replace("$", "")

df["Freight Cost (USD)"] = pd.to_numeric(df["Freight Cost (USD)"], errors="coerce")

df = df.dropna(subset=["Freight Cost (USD)"])

top10 = df.groupby("Country")["Freight Cost (USD)"] \
    .sum() \
    .sort_values(ascending=False) \
    .head(10)

top10 = top10 / 1_000_000

plt.figure(figsize=(10,6))
top10.plot(kind="bar")

plt.title("Top 10 Country")
plt.xlabel("Country")
plt.ylabel("Total Freight Cost (USD)")
plt.xticks(rotation=45)

plt.legend(["Cost * 1.000.000"], loc="upper right")
plt.show()
plt.tight_layout()
plt.show()