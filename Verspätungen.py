from dataclasses import replace

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv('SCMS_Delivery_History_Dataset.csv')

df["Delivery Recorded Date"] = pd.to_datetime(df["Delivery Recorded Date"], format="mixed")
df["Scheduled Delivery Date"] = pd.to_datetime(df["Scheduled Delivery Date"], format="mixed")   #.dt.strftime("%d/%m/%Y")

df["Delivered to Client Date"] = pd.to_datetime(df["Delivered to Client Date"], format="mixed") #.dt.strftime("%d/%m/%Y")

df["Delay"] = df["Delivered to Client Date"] - df["Scheduled Delivery Date"]


# verspätet = größer 0 Tage
delayed = df[df["Delay"].dt.days > 0]

print("Verspätete Sendungen:", len(delayed))

delayed.to_excel("delayed.xlsx", index=False)