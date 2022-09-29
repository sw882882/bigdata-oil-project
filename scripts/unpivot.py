import pandas as pd

inputFile = input("desired csv file: ")
df = pd.read_csv(inputFile)

df_list = list(df)
df_list.remove("Regions")

outputFile = input("desired output file: ")
pd.melt(df, id_vars = ["Regions"], value_vars = df_list).to_csv(outputFile)
print("complete, exiting...")    
