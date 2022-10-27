import plotly.graph_objects as go
import pandas as pd
import plotly.offline as offline
print("starting...")
df = pd.read_excel(
    "cleaned data/oil/processed Annual crude and lease condensate exports.xlsx"
)
year = df.at[1, "year"]
df_one_year = []
data_slider = []
while year <= df["year"].tolist()[-1]:
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
        df_one_year.append(df.iat[yearLocation[yy], 4])
        yy += 1
    yearLocation.clear()

    data_one_year_dict = dict(
        type="choropleth",
        locations=df["ISO_3_codes"],
        z=df_one_year,
        locationmode="ISO-3",
        colorscale="Reds",
    )

    data_slider.append(data_one_year_dict)

    df_one_year.clear()
    year += 1


steps = []
for i in range(len(data_slider)):
    step = dict(
        method="restyle",
        args=["visible", [False] * len(data_slider)],
        label="Year {}".format(i + df.at[1, "year"]),
    )
    step["args"][1][i] = True
    steps.append(step)

# I create the 'sliders' object from the 'steps'

sliders = [dict(active=0, pad={"t": 1}, steps=steps)]

# TODO: adapt the year dict into slider

layout = dict(

    geo=dict(
        scope="world",
    ),
    sliders=sliders,
)

geo = dict(
        showcountries=True,
        countrycolor="RebeccaPurple"
        )

fig = dict(data=data_slider, layout=layout, geo=geo)

offline.plot(
    fig,
    auto_open=True,
    image_filename="oil_exports",
    filename="./output.html",
    validate=True,
)


"""
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
    sliders=sliders,
)

fig.show()
"""
