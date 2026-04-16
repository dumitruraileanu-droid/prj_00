from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
from Verspätungen import delayed
import pandas as pd

plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))


delayed['Weight (Kilograms)'] = pd.to_numeric(delayed['Weight (Kilograms)'], errors="coerce")
delayed.groupby("Vendor")['Weight (Kilograms)'].sum().sort_values(ascending=False).head(10).plot(kind="bar", color="orange")

plt.xlabel("Shipment Mode")
plt.xticks(rotation=45, ha="right")
plt.ylabel("Weight (Kilograms)")

plt.tight_layout()
plt.show()