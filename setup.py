from setuptools import setup, find_packages
import codecs
import os

current_dir = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(current_dir, "README.md"), encoding="utf-8") as file:
  long_description = "\n" + file.read()

VERSION = '1.1.2'
DESCRIPTION = 'WebScraping library that scrapes & gathers data from multiple sources on the internet'

setup(
  name="webgraze",
  version=VERSION,
  author="shivendra",
  author_email="shivharsh44@gmail.com",
  description=DESCRIPTION,
  long_description=long_description,
  long_description_content_type="text/markdown",
  license="MIT",
  packages=find_packages(),
  keywords=["webscraping", "scraping", "webscraping library", "web scraping", "python webscraping", "beautifulsoup", "selenium"],
  classifiers=[
    "Development Status :: 1 - Planning",
    "Intended Audience :: Developers",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "License :: OSI Approved :: MIT License",
  ],
  install_requires=[
    "bs4",
    "tqdm",
    "google-api-python-client",
    "requests",
    "youtube-transcript-api",
    "selenium",
    "webdriver-manager",
  ],
)