import os
current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)

from graze import Unsplash
from graze.queries import Queries

topics = Queries("images")

image = Unsplash(directory='../images', metrics=True)
image(topics=topics())