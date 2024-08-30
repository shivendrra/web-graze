import os
import json
current_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_dir)

with open(f"./topics.json", "r") as infile:
  queries = json.load(infile)

error_msg = (
  "can't identify the category:\n"
  "Choose 'channel' for YouTube ChannelIds\n"
  "'search' for Britannica or Wikipedia search topics\n"
  "'images' for Unsplash & Pexels search topics"
)

class Queries:
  def __init__(self, category:str) -> None:
    self.category = category

  def __call__(self) -> list:
    if self.category == "search":
      return queries["search_topics"]
    elif self.category == "channel":
      return queries["channel_ids"]
    else:
      raise TypeError(error_msg)