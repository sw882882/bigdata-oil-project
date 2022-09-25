import pandas as pd

inputFile = input("desired csv file: ")
df = pd.read_csv(inputFile)
df = df.reset_index(drop=False)

row = input("row: ")
row = int(row)

rowCount = df.shape[0]
print(rowCount)
iterationCount = input("iteration count: ")
iterationCount = int(iterationCount)
#print(df.iat[(number on the row-2), number on the column-1])
#reference example

while rowCount > row:
    df.iat[row, 2] = None
    row += iterationCount + 1

outputFile = input("desired output file: ")
df.to_csv(outputFile, index=False)
print("complete, exiting...")    
