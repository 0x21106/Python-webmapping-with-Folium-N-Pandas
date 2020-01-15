import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = data["LAT"]
lon = data["LON"]
elev = data["ELEV"]

def color_changer(g):
    if g < 1000:
        return "green"
    elif g > 1000 and g < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[38.58, -99.09], zoom_start=5, tils="Stamen Terrain")

fg = folium.FeatureGroup(name="Markers")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], popup = "{} m".format(str(el)), radius = 6, fill_color=color_changer(el), fill_opacity = 0.7, color = "grey" ))
    
map_filter = folium.FeatureGroup(name="Filter")
map_filter.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(), style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 1000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg)
map.add_child(map_filter)

map.add_child(folium.LayerControl())

map.save("map.html")