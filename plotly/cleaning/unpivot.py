import pandas as pd

inputFile = "./data.csv"
df = pd.read_csv(inputFile)

df_list = list(df)
df_list.remove("region")
df_list.remove("ISO_3_codes")

output_df = pd.melt(df, id_vars=["region", "ISO_3_codes"], value_vars=df_list)
output_df.to_csv("output.csv")

print("complete, exiting...")
