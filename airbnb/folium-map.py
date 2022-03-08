##folium 
#base map

import folium
map_folium = folium.Map([1.35255,103.82580], zoom_start=11.4) 

#heatmap layer 

lat_and_long = []
for row in singapore_airbnb_listings:
    lat = row[10]
    long = row[11]
    
    lat_and_long.append([lat,long])
    
import folium
from folium.plugins import HeatMap

base_map = folium.Map([1.35255,103.82580], zoom_start=11.4)

HeatMap(lat_and_long, radius=8, gradient={0.2:'blue',0.4:'purple',0.6:'orange',1.0:'red'}).add_to(base_map)
display(base_map)

#price_of_property with tooltip
lat_long = []
listing_price = []
for row in singapore_airbnb_listings:
    
    lat_long.append([row[10],row[11]])
    listing_price.append(row[15]
# first 10 lat_long
lat_long_10 = lat_long[:10]
price_10 = listing_price[:10]

print(price_10)
                         

map_folium = folium.Map([1.35255,103.82580], zoom_start=11.4)
for i in range(0,len(lat_long_10)):   
    lat_long_of_one_listing = lat_long_10[i]    # Get a pair of lat and long
    pop_display_price = '$' + str(price_10[i])  # Get the price of listing and format the string
    tooltip = 'Click Me!'
    folium.Marker(lat_long_of_one_listing, popup=pop_display_price, tooltip=tooltip).add_to(map_folium)
    
display(map_folium)
                         
#density visualisation

from folium.plugins import MarkerCluster       # Import the MarkerCluster folium plugin

map_folium = folium.Map([1.35255,103.82580], zoom_start=11.4)

# Create a layer to store all the marker cluster
marker_cluster = MarkerCluster().add_to(map_folium)

for i in range(0,len(lat_long_10)):
    
    lat_long_of_one_listing = lat_long_10[i]    # Get a pair of lat and long
    pop_display_price = '$' + str(price_10[i])  # Get the price of listing and format the string
    
    # Create a marker object, and add it to marker cluster
    folium.Marker(
        location=lat_long_of_one_listing,
        popup=pop_display_price,
        icon=None,
    ).add_to(marker_cluster)

display(map_folium)
                         
### extract lat_long_price
def extract_lat_long_price(database):
    
    lat_long = []
    listing_price = []

    for row in singapore_airbnb_listings:

        lat_long.append([row[10],row[11]])
        listing_price.append(row[15])
        

    return lat_long, listing_price
    
extract_lat_long_price(singapore_airbnb_listings)
                         

                         
map_folium = folium.Map([1.35255,103.82580], zoom_start=11.4)
marker_cluster = MarkerCluster().add_to(map_folium)
for i in range(0,len(lat_long)):   
    lat_long_of_one_bnb = lat_long[i]    # Get a pair of lat and long
    pop_display_price = '$' + str(listing_price[i])  # Get the price of listing and format the string
    

    folium.Marker(
        location=lat_long_of_one_bnb,
        popup=pop_display_price,
        icon=None,
    ).add_to(marker_cluster)

display(map_folium)
