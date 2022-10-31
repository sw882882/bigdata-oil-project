import pandas as pd
import glob

files = glob.glob("./*.xlsx")

print(files)

for file in files:
    df = pd.read_excel(file)
    for i in range(len(df)):
        if df.at[i, "region"] == "South Korea":
            print("foo")
            df.at[i, "ISO_3_codes"] = "KOR"

    df.to_excel("output/" + file, index=False)
    print("complete")
