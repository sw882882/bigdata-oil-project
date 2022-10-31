import plotly.express as px
import pandas as pd
import io
import PIL

print("starting...")
df = pd.read_excel(
    #"/home/andrew/repo-projects/projects/bigdata-oil-project/plotly/cleaned data/oil/fixednamesdata/Annual Petroleum and other Liquids Production/Annual Petroleum and other Liquids Production - Crude Oil(Mbd).xlsx"
    # "/home/andrew/repo-projects/projects/bigdata-oil-project/plotly/cleaned data/oil/processed Annual crude and lease condensate exports.xlsx"
    "/home/andrew/repo-projects/projects/bigdata-oil-project/plotly/cleaned data/oil/processed Annual crude and lease condensate imports.xlsx"
)

colorscale = [[0, "gray"], [0.01, "gray"], [0.01, "blue"], [1, "red"]]

fig = px.choropleth(
    df,
    animation_frame="year",
    animation_group="region",
    locations="ISO_3_codes",
    color="value",
    hover_name="region",
    color_continuous_scale=colorscale,
)

fig.update_geos(showcountries=True, countrycolor="Black")

fig.update_layout(
    title_text="Global crude oil production by year",
    geo_scope="world",  # limite map scope to USA
)


# generate images for each step in animation
frames = []
for s, fr in enumerate(fig.frames):
    # set main traces to appropriate traces within plotly frame
    fig.update(data=fr.data)
    # move slider to correct place
    fig.layout.sliders[0].update(active=s)
    # generate image of current state
    frames.append(PIL.Image.open(io.BytesIO(fig.to_image(format="png"))))

# create animated GIF
frames[0].save(
    "test.gif",
    save_all=True,
    append_images=frames[1:],
    optimize=True,
    duration=500,
    loop=0,
)
