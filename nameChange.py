import pandas as pd

inputFile = input("desired csv file: ")
df = pd.read_csv(inputFile)
df = df.reset_index(drop=False)

row = 4

rowCount = df.shape[0]
print(rowCount)
iterationCount = input("iteration count: ")
#print(df.iat[(number on the row-2), number on the column-1])
#reference example

while rowCount > row:
    regionName = df.iat[(row - 1 - 2), 1]
    for x in range(int(iterationCount)):
        df.iat[(row - 2), 0] = regionName
        row += 1
    row += 1

outputFile = input("desired output file: ")
df.to_csv(outputFile)
print("complete, exiting...")    
