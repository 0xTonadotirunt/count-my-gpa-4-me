import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

ukraine_df = pd.read_csv('data/ukrainian_conflicts_comments.csv')


collection_of_words =''
for row in ukraine_title.title:
    collection_of_words += row + " "
    
collection_of_words = collection_of_words.replace("Comment","")
    
print(collection_of_words)

wordcloud = WordCloud(max_words=400, background_color='black').generate(collection_of_words)
plt.figure(figsize=(25,20))

# Display the image
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
