import pandas as pd
import glob


print("Starting...")


def cleanup_df(file):
    print("cleaning dataframe...")
    print(file)
    columnName = file[(file.rfind("/") + 1) :]
    print(columnName)

    df = pd.read_excel(file)
    print("first")
    print(df.columns.tolist())
    if (len(df.columns.tolist()) == 5):
        df.drop(df.columns[[0, 1]], axis=1, inplace=True)
    else:
        df.drop(df.columns[0], axis=1, inplace=True)

    df = df.rename(columns={"value": columnName})

    print("dataframe cleaning complete")

    print(df.columns.tolist())
    return df


files = glob.glob("./**/*.xlsx") + glob.glob("./oil/fixednamesdata/**/*.xlsx")
print(files)

# get a starting output dataframe

output_df = pd.read_excel(files[0])
output_df.drop(output_df.columns[0], axis=1, inplace=True)

firstFileName = str(files[0])

tempcolumnName = firstFileName[(firstFileName.rfind("/") + 1) :]
print(tempcolumnName)

output_df = output_df.rename(columns={"value": tempcolumnName})

merge_df = cleanup_df(files[1])

output_df = pd.merge(output_df, merge_df, how="left", on=["ISO_3_codes", "year"])

for i in range(len(files[:2])):
    merge_df = cleanup_df(files[i + 2])
    output_df = pd.merge(output_df, merge_df, how="left", on=["ISO_3_codes", "year"])
    print("merged")

output_df.to_csv("output.csv")
# df1 = pd.read_excel(filedialog.askopenfilename(), index_col=False)
# df1 = pd.read_csv("put here later")
# df1.drop(df1.columns[0], axis=1, inplace=True)
# df1.drop(columns="region", inplace=True)


# new_df = pd.merge(df1, df2, how="left", on=["ISO_3_codes", "year"])
# new_df.to_csv("output4.csv")
