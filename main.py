import pandas as pd
from config.const import MAC_ADDRESS_THRESHOLD, RSSI_THRESHOLD

# Load the data
df = pd.read_csv("./data/demo.csv")

# 条件に一致する行が存在するか判定
condition = (df["bssid"] == MAC_ADDRESS_THRESHOLD) & (df["rssi"] >= RSSI_THRESHOLD)
exists = condition.any()

print(f"Exists: {exists}")
