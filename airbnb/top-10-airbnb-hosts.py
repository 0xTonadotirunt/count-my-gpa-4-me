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
