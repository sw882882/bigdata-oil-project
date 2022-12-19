import pandas as pd
from pandas._config.config import register_option
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import country_converter as coco

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()


# replace example data with actual data
print("choose data 1")
file1 = filedialog.askopenfilename()
print(file1)
df1 = pd.read_excel(file1)
print("choose data 2")
file2 = "./cleaned data/wealth inequality/processed bottom50.xlsx"
print(file2)
df2 = pd.read_excel(file2)
df3 = pd.read_csv("./cleaned data/worldpop.csv")
file3 = "./cleaned data/wealth inequality/processed top10.xlsx"
df4 = pd.read_excel(file3)
file4 = "./cleaned data/wealth inequality/processed top1.xlsx"
df5 = pd.read_excel(file4)
file5 = "./cleaned data/gdp per capita/processed GDP_per_capita.xlsx"
df6 = pd.read_excel(file5)

startYear = 1995
endYear = 2014

columnName1 = file1[(file1.rfind("/") + 1) :]
columnName2 = file2[(file2.rfind("/") + 1) :]
columnName3 = "population"
columnName4 = file3[(file3.rfind("/") + 1) :]
columnName5 = file4[(file4.rfind("/") + 1) :]
columnName6 = file5[(file5.rfind("/") + 1) :]
columnName1 = columnName1.replace(".xlsx", "")
columnName1 = columnName1.replace("processed ", "")
columnName2 = columnName2.replace(".xlsx", "")
columnName2 = columnName2.replace("processed ", "")
columnName4 = columnName4.replace(".xlsx", "")
columnName4 = columnName4.replace("processed ", "")
columnName5 = columnName5.replace(".xlsx", "")
columnName5 = columnName5.replace("processed ", "")
columnName6 = columnName6.replace(".xlsx", "")
columnName6 = columnName6.replace("processed ", "")
print(columnName1)
print(columnName2)

df1 = df1.truncate(before=df1.index[df1["year"] == startYear].tolist()[0])
df1 = df1.truncate(after=df1.where(df1 == endYear).last_valid_index())
df2 = df2.truncate(before=df2.index[df2["year"] == startYear].tolist()[0])
df2 = df2.truncate(after=df2.where(df2 == endYear).last_valid_index())
df4 = df4.truncate(before=df4.index[df4["year"] == startYear].tolist()[0])
df4 = df4.truncate(after=df4.where(df4 == endYear).last_valid_index())
df5 = df5.truncate(before=df5.index[df5["year"] == startYear].tolist()[0])
df5 = df5.truncate(after=df5.where(df5 == endYear).last_valid_index())
df6 = df6.truncate(before=df6.index[df6["year"] == startYear].tolist()[0])
df6 = df6.truncate(after=df6.where(df6 == endYear).last_valid_index())
# df3 = df3.truncate(before=df3.index[df3["year"] == startYear].tolist()[0])
# df3 = df3.truncate(after=df3.where(df3 == endYear).last_valid_index())


df1.drop(df1.columns[0], axis=1, inplace=True)
if len(df2.columns.tolist()) == 5:
    df2.drop(df2.columns[[0, 1]], axis=1, inplace=True)
else:
    df2.drop(df2.columns[0], axis=1, inplace=True)

if len(df4.columns.tolist()) == 5:
    df4.drop(df4.columns[[0, 1]], axis=1, inplace=True)
else:
    df4.drop(df4.columns[0], axis=1, inplace=True)
if len(df5.columns.tolist()) == 5:
    df5.drop(df5.columns[[0, 1]], axis=1, inplace=True)
else:
    df5.drop(df5.columns[0], axis=1, inplace=True)
if len(df6.columns.tolist()) == 6:
    df6.drop(df6.columns[[0, 1]], axis=1, inplace=True)
else:
    df6.drop(df6.columns[0], axis=1, inplace=True)
# df3.drop(df3.columns[[0, 1]], axis=1, inplace=True)

df1 = df1.rename(columns={"value": columnName1})
df2 = df2.rename(columns={"value": columnName2})
df4 = df4.rename(columns={"value": columnName4})
df5 = df5.rename(columns={"value": columnName5})
df6 = df6.rename(columns={"value": columnName6})
# df3 = df3.rename(columns={"value": columnName3})

# df1[columnName1] = df1[columnName1] / df3["value"]

# limit countries
countries = [
    "USA",
    "AUS",
    "SAU",
    "CAN",
    "IND",
    "RUS",
    "ZAF",
    "TUR",
    "ARG",
    "BRA",
    "MEX",
    "FRA",
    "DEU",
    "ITA",
    "GBR",
    "CHN",
    "KOR",
    "JPN",
    "IDN",
    # non g-20 countries
    "AZE",
    "VEN",
    "SGP",
    "IRN",
    "QAT",
    "ARE",
    "KWT",
    "NOR",
    "BRN",
    "KAZ",
    "OMN",
    "LBY",
]

df1 = df1[df1["ISO_3_codes"].isin(countries)]
df2 = df2[df2["ISO_3_codes"].isin(countries)]
df4 = df4[df4["ISO_3_codes"].isin(countries)]
df5 = df5[df5["ISO_3_codes"].isin(countries)]
df6 = df6[df6["ISO_3_codes"].isin(countries)]


output_df = pd.merge(df1, df2, how="left", on=["ISO_3_codes", "year"])
figd = make_subplots(specs=[[{"secondary_y": True}]])

for country in countries:
    output_dftemp = output_df[output_df["ISO_3_codes"] == country]
    countryName = coco.convert(names=[country], to="name_short")
    figd.add_trace(
        go.Scatter(
            x=output_dftemp["year"],
            y=output_dftemp[list(df2)[-1]],
            name=countryName + " primary axis",
        ),
        secondary_y=False,
    )
    figd.add_trace(
        go.Scatter(
            x=output_dftemp["year"],
            y=output_dftemp[columnName1],
            name=countryName + " secondary axis",
        ),
        secondary_y=True,
    )

figd.update_layout(
    yaxis_range=[0, 1],
    title_text="Bottom 50% wealthshare correlated with " + columnName1,
)
figd.update_xaxes(title_text="year")
figd.update_yaxes(
    title_text="Percentage of wealth held by the bottom 50% in terms of wealth",
    secondary_y=False,
)
figd.update_yaxes(title_text=columnName1, secondary_y=True)
figd.show()

figd.write_html("./graphs/" + columnName1 + " correlated with " + columnName2 + ".html")


output_df = pd.merge(df1, df4, how="left", on=["ISO_3_codes", "year"])
figd = make_subplots(specs=[[{"secondary_y": True}]])

for country in countries:
    output_dftemp = output_df[output_df["ISO_3_codes"] == country]
    countryName = coco.convert(names=[country], to="name_short")
    figd.add_trace(
        go.Scatter(
            x=output_dftemp["year"],
            y=output_dftemp[list(df4)[-1]],
            name=countryName + " primary axis",
        ),
        secondary_y=False,
    )
    figd.add_trace(
        go.Scatter(
            x=output_dftemp["year"],
            y=output_dftemp[columnName1],
            name=countryName + " secondary axis",
        ),
        secondary_y=True,
    )


figd.update_layout(
    yaxis_range=[0, 1], title_text="Top 10% wealthshare correlated with " + columnName1
)
figd.update_xaxes(title_text="year")
figd.update_yaxes(
    title_text="Percentage of wealth held by the top 10% in terms of wealth",
    secondary_y=False,
)
figd.update_yaxes(title_text=columnName1, secondary_y=True)
figd.show()


figd.write_html("./graphs/" + columnName1 + " correlated with " + columnName4 + ".html")


output_df = pd.merge(df1, df5, how="left", on=["ISO_3_codes", "year"])
figd = make_subplots(specs=[[{"secondary_y": True}]])

for country in countries:
    output_dftemp = output_df[output_df["ISO_3_codes"] == country]
    countryName = coco.convert(names=[country], to="name_short")
    figd.add_trace(
        go.Scatter(
            x=output_dftemp["year"],
            y=output_dftemp[list(df5)[-1]],
            name=countryName + " primary axis",
        ),
        secondary_y=False,
    )
    figd.add_trace(
        go.Scatter(
            x=output_dftemp["year"],
            y=output_dftemp[columnName1],
            name=countryName + " secondary axis",
        ),
        secondary_y=True,
    )

figd.update_layout(
    yaxis_range=[0, 1], title_text="Top 1% wealthshare correlated with " + columnName1
)
figd.update_xaxes(title_text="year")
figd.update_yaxes(
    title_text="Percentage of wealth held by the top 1% in terms of wealth",
    secondary_y=False,
)
figd.update_yaxes(title_text=columnName1, secondary_y=True)
figd.show()

figd.write_html("./graphs/" + columnName1 + " correlated with " + columnName5 + ".html")


output_df = pd.merge(df1, df6, how="left", on=["ISO_3_codes", "year"])
figd = make_subplots(specs=[[{"secondary_y": True}]])

for country in countries:
    output_dftemp = output_df[output_df["ISO_3_codes"] == country]
    countryName = coco.convert(names=[country], to="name_short")
    figd.add_trace(
        go.Scatter(
            x=output_dftemp["year"],
            y=output_dftemp[list(df6)[-1]],
            name=countryName + " primary axis",
        ),
        secondary_y=False,
    )
    figd.add_trace(
        go.Scatter(
            x=output_dftemp["year"],
            y=output_dftemp[columnName1],
            name=countryName + " secondary axis",
        ),
        secondary_y=True,
    )

figd.update_layout(
    yaxis_range=[0, 120000], title_text="GDP per capita correlated with " + columnName1
)
figd.update_xaxes(title_text="year")
figd.update_yaxes(title_text="GDP per capita in USD" +" (" + "2022-7-20" + ")", secondary_y=False)
figd.update_yaxes(title_text=columnName1, secondary_y=True)
figd.show()

figd.write_html("./graphs/" + columnName1 + " correlated with " + columnName6 + ".html")
