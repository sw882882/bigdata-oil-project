import pandas as pd

inputFile = input("desired csv file: ")
df = pd.read_csv(inputFile)

df.dropna(how = "all", inplace = True)

outputFile = input("desired output file: ")
df.to_csv(outputFile)
print("complete, exiting...")    
