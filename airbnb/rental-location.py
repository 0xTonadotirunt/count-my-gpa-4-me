# Run this cell to load the Airbnb dataset into a nested list
import csv

singapore_airbnb_listings = []

# Read the first csv file into nested list
with open('data/singapore_airbnb_listings.csv', newline='', encoding='utf8') as f:
    reader = csv.reader(f)
    for row in reader:
        singapore_airbnb_listings.append(row)

    # Remove header
    singapore_airbnb_dataheaders = singapore_airbnb_listings[0]
    singapore_airbnb_listings = singapore_airbnb_listings[1:]
    


# Loop through the airbnb listings to clean the data
for row in singapore_airbnb_listings:
    
    # Extract the data and store into variables for easy access
    host_total_listings_count = row[8]
    longitude = row[10]
    latitude = row[11]
    price = row[15]
    cleaning_fee = row[16]
    review_scores_rating = row[17]
    reviews_per_month = row[18]
    
    # host_total_listings_count (convert to float)
    if host_total_listings_count ==  '':
        row[8] = 0
    else:
        row[8] = float(host_total_listings_count) 
    
    # longitude and latitude (convert to float)
    row[10] = float(longitude) 
    row[11] = float(latitude)
    
    # price (convert to float)
    if price == '':
        row[15] = 0 
    else:
        row[15] = float(price)

    # cleaning fee (convert to float)
    if cleaning_fee == '':
        row[16] = 0 
    else:
        row[16] = float(cleaning_fee)
    
    # review scores rating (convert to float)
    if review_scores_rating == '':
        row[17] = 0 
    else:
        row[17] = float(review_scores_rating)
    
    # review per month(convert to float)
    if reviews_per_month == '':
        row[18] = 0 
    else:
        row[18] = float(reviews_per_month)
        
    

#conver to pandas
singapore_airbnb_df = pd.DataFrame(singapore_airbnb_listings, columns = singapore_airbnb_dataheaders)
singapore_airbnb_df.head()

#create dictionary of the number of times a district appears
neighbourhood_counts = {}

for row in singapore_airbnb_listings:
    neighbourhood = row[9]
    if neighbourhood in neighbourhood_counts:
        neighbourhood_counts[neighbourhood] += 1
        
    else:
        neighbourhood_counts[neighbourhood] = 1
        
        
#see the dictionary in sorted order
import operator
sorted_neighbourhood_listings = dict(sorted(neighbourhood_counts.items(), key=operator.itemgetter(1),reverse=True))
print(sorted_neighbourhood_listings)

#separate dictionary key and count
neighbour_listings = list(sorted_neighbourhood_listings.keys())
neighbour_num_listings = list(sorted_neighbourhood_listings.values())

#top ten
neighbour_listings = neighbour_listings[:10]
neighbour_num_listings = neighbour_num_listings[:10]
        
print(neighbourhood_counts)

###top 10 airbnb hosts with the most listing
host_listings = {}

# Count number of listings for each host ID
for row in singapore_airbnb_listings:
    
    host_id = row[6]
    
    if host_id in host_listings:
        
        host_listings[host_id] += 1
        
    else:
        
        host_listings[host_id] = 1

# Sort host_listings in descending order
import operator
sorted_host_listings = dict(sorted(host_listings.items(), key=operator.itemgetter(1),reverse=True))


# Convert dictionary into 2 lists, and slice them to get top 10 host ID & listing count

host_id = list(sorted_host_listings.keys())
host_num_listings = list(sorted_host_listings.values())

top_10_host_id = host_id[:10]
top_10_num_listings = host_num_listings[:10]

##visualisation
#bargraph top ten host

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.bar(host_id_listings, host_id_num_listings)
ax.set_ylabel("Number of Listings")
ax.set_xlabel("Host ID")
ax.set_title("Listings of top 10 host")
ax.set_xticklabels(host_id_listings, rotation=45)
plt.show()

#Piechart roomtype
room_type = list(room_type_counts.keys())
num_room = list(room_type_counts.values())

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
fig, ax = plt.subplots()
ax.pie(num_room, labels=room_type, autopct='%1.1f%%',shadow=True, startangle=45) #starts at shared room

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')  

# To add legend
ax.legend(room_type,
          title="Room Type",
          loc="center left",
          bbox_to_anchor=(1, 0))

plt.show()

#piechart property type

property_type_listings = {}
for row in singapore_airbnb_listings:
    propety_type = row[12]
    if propety_type in property_type_listings:       
        property_type_listings[propety_type] += 1      
    else:   
        property_type_listings[propety_type] = 1
        
property_type_listings = dict(sorted(property_type_listings.items(), key=operator.itemgetter(1),reverse=True))
property_type_names = list(property_type_listings.keys())
property_type_values = list(property_type_listings.values())
#top 5
property_type_names = property_type_names[:5]
property_type_values = property_type_values[:5]

fig, ax = plt.subplots()
ax.pie(property_type_values, labels=property_type_names, autopct='%1.1f%%',shadow=True, startangle=45)
ax.legend(property_type_listings,
          title="Property Type",
          loc="center left",
          bbox_to_anchor=(1, 0))
plt.show()

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
