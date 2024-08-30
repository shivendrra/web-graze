from graze import Unsplash, Wikipedia

wiki = Wikipedia(filepath='../data.txt', metrics=True)
wiki(queries=['antarctica', 'europe', 'america'])