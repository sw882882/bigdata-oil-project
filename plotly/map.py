import plotly.graph_objects as go
import pandas as pd

df = pd.read_excel(
    "cleaned data/oil/processed Annual crude and lease condensate exports.xlsx"
)
year = df.at(1, "year")
dfdata = []
data_slider = {}
while year <= df["year"].tail(1):
    y = 1
    yearLocation = []
    while df["value"].tolist():
        if y >= len(df.index):
            break
        if df.iat[y, 3] == year:
            yearLocation.append(y)
        y += 1

    yy = 0
    while yearLocation:
        if yy >= len(yearLocation):
            break
        dfdata.append(df.iat[yearLocation[yy], 4])
        yy += 1
    yearLocation.clear()
    appendDict = {
                str(year): dfdata
            }
    data_slider.append(appendDict)
    appendDict.clear()
    dfdata.clear()
    year += 1


# TODO: adapt the year dict into slider
fig = go.Figure(
    data=go.Choropleth(
        locations=df["ISO_3_codes"],  # iso code country names
        z=dfdata,
        locationmode="ISO-3",
        colorscale="Reds",
        colorbar_title="Crude Oil (including lease condensate exports), Mb/d",
    )
)


fig.update_geos(showcountries=True, countrycolor="RebeccaPurple")

fig.update_layout(
    title_text="Global crude oil exports 2003",
    geo_scope="world",  # limite map scope to USA
)

fig.show()
