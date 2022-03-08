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
