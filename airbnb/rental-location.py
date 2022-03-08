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

#visualisation : bar graph.png

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.bar(host_id_listings, host_id_num_listings)

ax.set_ylabel("Number of Listings")
ax.set_xlabel("Host ID")
ax.set_title("Listings of top 10 host")

ax.set_xticklabels(host_id_listings, rotation=45)
plt.show()
