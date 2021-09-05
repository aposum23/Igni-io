import geopandas as gpd
import pandas as pd
shapefile = gpd.read_file("validate_public.shp")
ans = shapefile[['fireid', 'geometry', ]]
ans.to_excel("output.xlsx")
