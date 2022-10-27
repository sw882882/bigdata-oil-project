import plotly.express as px
import pandas as pd
import plotly.offline as offline

print("starting...")
df = pd.read_excel(
    "cleaned data/oil/processed Annual crude and lease condensate exports.xlsx"
)
fig = px.choropleth(
    df,
    animation_frame="year",
    animation_group="region",
    locations="ISO_3_codes",
    color="value",
    hover_name="region",
    color_continuous_scale=px.colors.sequential.Plasma,
)

fig.update_geos(showcountries=True, countrycolor="RebeccaPurple")

fig.update_layout(
    title_text="Global crude oil exports by year",
    geo_scope="world",  # limite map scope to USA
)

fig.show()
