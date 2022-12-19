import pandas as pd

df = pd.read_excel("./processed top1.xlsx")

df = df[df.region != "Other Russia & Central Asia"]
df = df[df.region != "Russia & Central Asia"]
print("Other Russia & Central Asia (at market exchange rate)")
df = df[
    df.region != "Other Russia & Central Asia (at market exchange rate)"
]
df.to_excel("output.xlsx")
