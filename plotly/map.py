import plotly.graph_objects as go
import pandas as pd

df = pd.read_excel('cleaned data/oil/processed Annual crude and lease condensate exports.xlsx')

y = 1
yearLocation = []
while df['value'].tolist():
    if df.iat[3,y] == "2000":
        yearLocation.append(y)
    y += 1

data = []  
while yearLocation:
    data.append(df.iat[4,y])
    
fig = go.Figure(data = go.Choropleth(
    locations = df['ISO_3_codes'], #iso code country names
    z = data,
    locationmode = "ISO-3",
    colorscale = 'Reds',
    colorbar_title = "Crude Oil (including lease condensate exports), Mb/d"
))

fig.update_layout(
    title_text = "Global crude oil exports 2000",
    geo_scope='world', # limite map scope to USA
)

fig.show()



    
