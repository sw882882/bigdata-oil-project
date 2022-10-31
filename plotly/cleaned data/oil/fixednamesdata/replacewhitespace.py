import pandas as pd
import glob
import numpy as np


# files = glob.glob("./*.xlsx")
files = "~/repo-projects/projects/bigdata-oil-project/plotly/cleaned data/oil/fixednamesdata/Annual Refined Petroleum Products Consumption/Annual Refined Petroleum Products Consumption - TOTAL Consumption of Refined Petroleum Products (Mbd).xlsx"
print(files)

df = pd.read_excel(files)
# df.replace(r'^\s*$', np.nan, regex=True, inplace=True)

print(df["value"].apply(pd.to_numeric, errors='coerce'))

# df.to_excel("output/" + "output.xlsx", index=False)
# print("complete")
