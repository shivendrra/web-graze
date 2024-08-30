from graze import Unsplash
# from graze.queries import Queries

# queries = Queries(category="search")
# print(queries())
image = Unsplash(directory='../images')
image(topics=['cars'])