import folium
map = folium.Map(location=[38.63, -90.20], zoom_start=6, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for coordinates in [[33.75, -84.34], [35.75, -80.38]]:
    fg.add_child(folium.Marker(location=coordinates, popup="I created this marker", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")
