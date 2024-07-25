"""
  --> contains some sample search queries for the britannica scrapper
"""

class searchQueries:
  def __init__(self):
    self.search_queries = [
      "antarctica", "colonization", "world war", "asia", "africa", 
      "australia", "holocaust", "voyages", "biological viruses", 
      "Martin Luther King Jr", "Abraham Lincoln", "Quarks", "Quantum Mechanics", 
      "Biological Viruses", "Drugs", "Rockets", "Physics", "Mathematics", 
      "nuclear physics", "nuclear fusion", "CRISPR CAS-9", "virginia woolf", 
      "cocaine", "marijuana", "apollo missions", "birds", "blogs", "journal", 
      "Adolf Hitler", "Presidents of United States", "genders and sexes", 
      "journalism", "maths theories", "matter and particles", "discoveries", 
      "authors and writers", "poets and novel writers", "literature", "awards and honors",
      "climate change", "renewable energy", "artificial intelligence", "machine learning", 
      "blockchain technology", "cryptocurrencies", "space exploration", "Mars missions", 
      "black holes", "string theory", "evolution", "human genome project", "stem cells", 
      "pandemics", "influenza", "COVID-19", "vaccination", "genetic engineering", 
      "nanotechnology", "3D printing", "cybersecurity", "quantum computing", 
      "robotics", "drones", "self-driving cars", "electric vehicles", "smart cities", 
      "internet of things", "big data", "cloud computing", "augmented reality", 
      "virtual reality", "mixed reality", "social media", "digital marketing", 
      "e-commerce", "fintech", "global warming", "deforestation", "ocean acidification", 
      "biodiversity", "conservation", "sustainable agriculture", "organic farming", 
      "hydropower", "solar energy", "wind energy", "geothermal energy", "tidal energy", 
      "nuclear power", "space tourism", "interstellar travel", "terraforming", 
      "exoplanets", "SETI", "astrobiology", "dark matter", "dark energy", 
      "the big bang theory", "cosmic microwave background", "multiverse", "extraterrestrial life"
    ]
    
  def __call__(self):
    return self.search_queries