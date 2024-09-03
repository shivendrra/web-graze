from setuptools import setup, find_packages
import codecs
import os

current_dir = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(current_dir, "README.md"), encoding="utf-8") as file:
  long_description = "\n" + file.read()

with open("requirements.txt", encoding="utf-8") as f:
  required = f.read().splitlines()

VERSION = '1.1.2'
DESCRIPTION = 'WebScraping library that scrapes & gathers data from multiple sources on the internet'

setup(
  name="webgraze",
  version=VERSION,
  author="shivendra",
  author_email="<shivharsh44@gmail.com>",
  description=DESCRIPTION,
  long_description=long_description,
  long_description_content_type="text/markdown",
  license="MIT",
  packages=find_packages(),
  keywords=["webscraping", "scraping", "webscraping library", "web scraping", "python webscraping", "beautifulsoup", "selenium"],
  classifiers=[
    "Development Status :: 1 - Planning",
    "Intended Audience :: Developers",
    "Programing Language :: Python",
    "Operating System :: Windows"
  ],
  install_requires=required,
)