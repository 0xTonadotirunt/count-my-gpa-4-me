singapore_airbnb_listings
# Extract the longitudes, latitudes and review scores into separate lists
long = []
lat = []
reviews_score = []

for row in singapore_airbnb_listings:
    long.append(row[11])
    lat.append(row[10])
    reviews_score.append(row[17])
    
    
# Import image of Singapore
singapore_img = plt.imread('img/singapore_image.png')

# Create fig and ax
fig, ax = plt.subplots(figsize=(18,12)) # Configure the combined figure size of all subplots

# Generate scatter plot
scatter_plot_obj = ax.scatter(long, lat,
                              c=reviews_score,
                              cmap=plt.get_cmap("jet"),
                              vmin=min(reviews_score), 
                              vmax=max(reviews_score),
                              alpha=0.4)

# Set the title of the plot
plt.title('Reviews of Airbnb Listing in Singapore', fontsize=20)

# Set the ylabel and xlabel of plot
plt.ylabel('Latitude', fontsize=20)
plt.xlabel('Longitude', fontsize=20)

# Create the legend
cbar = plt.colorbar(mappable=scatter_plot_obj, ax=ax)

# Show the Singapore map
plt.imshow(singapore_img, extent=[103.5, 104, 1.15, 1.50], alpha=0.5)

# Display scatterplot
plt.show()
