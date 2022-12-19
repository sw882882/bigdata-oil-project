from numpy import NaN, nan
import pandas as pd
import glob

files = glob.glob("./*.xlsx")

print(files)

for file in files:
    df = pd.read_excel(file)
    for x in df["value"].tolist():
        if isinstance(x, (str, float, NaN, None, nan)):
            print(x)

print("complete")
