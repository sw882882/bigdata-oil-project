import country_converter as coco
import pandas as pd

cc = coco.CountryConverter()

df = pd.read_csv("./top10.csv")

countries = list(df["region"])

iso_names = coco.convert(names=countries, to="ISO3")

df["ISO_3_codes"] = iso_names
df.insert(1, "ISO_3_codes", df.pop("ISO_3_codes"))
df.replace({'not found': ''}, regex=True, inplace=True)


df.to_excel("./output.xlsx")
