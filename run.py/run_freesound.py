import os
current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("freesound_key")

from graze import Freesound

sound = Freesound(api_key=API_KEY, download_dir="audios", metrics=True)
sound(topics=["clicks", "background", "nature"])