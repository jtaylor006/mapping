import folium
map = folium.Map(location=[38.63, -90.20], zoom_start=6, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[33.75, -84.38], popup="I created this marker", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map1.html")
