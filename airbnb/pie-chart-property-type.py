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
