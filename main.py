import folium
import geopandas as gpd
import shapely.wkt


poli_str = "POLYGON((136.78666357 49.52418785,136.77954435 49.53637047,136.7894783 49.65238667,136.84280473 49.67015227,136.89674525 49.67134434,136.9043166 49.64856024,136.84841846 49.53733865,136.81105098 49.52899722,136.78666357 49.52418785))"
p = shapely.wkt.loads(poli_str)
sim_geo = gpd.GeoSeries(p)
cord = [sim_geo.centroid.y, sim_geo.centroid.x]
m = folium.Map(location=cord, zoom_start=13, tiles = "Stamen Terrain")
geo_j = sim_geo.to_json()
geo_j = folium.GeoJson(data=geo_j, style_function=lambda x: {'fillColor': 'red'})
geo_j.add_to(m)
m.save("map1.html")
