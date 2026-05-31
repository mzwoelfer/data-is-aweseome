import pandas as pd
import json
import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from helpers import open_json

coal_data = open_json("coal_data.json")

df = pd.DataFrame(coal_data)
df["time"] = pd.to_datetime(df["time"])
df_monthly = df.resample("ME", on="time").agg({"data": ["mean", "min", "max"]})

averages = df_monthly["data", "mean"]
minimums = df_monthly["data", "min"]
maximums = df_monthly["data", "max"]

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(averages.index, averages, label="Average")

ax.fill_between(averages.index, minimums, maximums, alpha=0.2, label="Min-Max Range")

ax.set_xlabel("Years")
ax.set_ylabel("Net Daily Coal Electricty Produced (TWh)")
ax.set_title("Average Daily Coal Production with Min-Max Range")

formatter = ticker.FuncFormatter(lambda x, pos: f"{x / 1e6:.1f}")
ax.yaxis.set_major_formatter(formatter)

ax.legend()
plt.show()

