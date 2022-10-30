import os
import pandas as pd


files = [f for f in os.listdir(".") if os.path.isfile(f)]
files.remove("seperatefile.py")

print(files)

for file in files:
    df = pd.read_excel(file)
    first = df.at[1, "product"]
    i = 0
    products = []
    while True:
        if i != 0:
            if df.at[(i + 1), "product"] == first:
                break
        i += 1

    print(file + " has " + str(i) + " products")

    for productnumber in range(i):
        df = pd.read_excel(file)
        g = 0
        df.loc[
            df["product"].ne(df.at[(productnumber, "product")]), :
        ] = ""

        """
        for lineNo in df["Unnamed: 0"].tolist():
            if g != 0:

                if (
                    df.at[(productnumber + 1), "product"]
                    != df.at[(lineNo + 1), "product"]
                ):
                    print(lineNo)
                    df1.drop([lineNo], inplace=True)
            g = 1
        """
        print(
            "./'"
            + (file.replace(".xlss", " ")).replace("'", "")
            + df.at[(i + 1), "product"]
            + ".xlsx'"
        )
        df.to_excel(
            "output/"
            + (file.replace(".xlsx", "")).replace(" ", "")
            + str(productnumber)
            + ".xlsx"
        )
        print("complete")
