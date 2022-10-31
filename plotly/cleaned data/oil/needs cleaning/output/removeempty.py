import pandas as pd
import glob

files = glob.glob("./*.xlsx")

print(files)

for file in files:
    df = pd.read_excel(file)
    df = df[df["product"].notna()]
    df.to_excel("output/" + file)
    print("complete")
