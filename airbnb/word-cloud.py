from wordcloud import WordCloud
import matplotlib.pyplot as plt

collection_of_description = ''

for row in singapore_airbnb_listings:
    
    collection_of_description += row[3] + ' '

    
# Print the first 200 characters of the string
print(collection_of_description[:200])



# Generate word cloud image
wordcloud = WordCloud(max_words=200, background_color='white').generate(collection_of_description)
plt.figure(figsize=(25,20))

# Display the image
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
