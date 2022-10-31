import pandas as pd
import glob
import numpy as np

files = glob.glob("./*.xlsx")

print(files)

for file in files:
    df = pd.read_excel(file)
    df.replace("--", np.nan, inplace=True)

    df.to_excel("output/" + file, index=False)
    print("complete")
