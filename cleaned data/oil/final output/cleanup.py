import pandas as pd
import glob

files = glob.glob("./*.xlsx")

print(files)

for file in files:
    df = pd.read_excel(file)
    title = df.at[5, "product"].replace(" ", "")

    df = df.drop(df.columns[[0, 1, 2, 5]], axis=1)

    df.to_excel(
        "output/"
        + file.replace(".xlsx", "")
        + title.replace("/", "∕")
        + ".xlsx"
    )
    print("complete")
