"""
  --> contains sample queries, similar to britannicaScrapper
"""

class WikiQueries:
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
      "the big bang theory", "cosmic microwave background", "multiverse", "extraterrestrial life",
      "neuroscience", "psychology", "behavioral economics", "cryptography", "linguistics", 
      "paleontology", "archaeology", "anthropology", "medieval history", "Renaissance art", 
      "Baroque music", "classical literature", "philosophy of science", "ethics", 
      "existentialism", "surrealism", "cubism", "impressionism", "romanticism", 
      "modernism", "postmodernism", "futurism", "dadaism", "expressionism", "neoclassicism", 
      "avant-garde", "minimalism", "pop art", "abstract art", "photorealism", "conceptual art", 
      "installation art", "performance art", "digital art", "cyberpunk", "steampunk", 
      "biopunk", "solarpunk", "architecture", "urban planning", "landscape architecture", 
      "industrial design", "fashion design", "graphic design", "web design", "interior design", 
      "product design", "animation", "film production", "video game design", "sound design", 
      "photography", "cinematography", "documentary filmmaking", "screenwriting", 
      "theater production", "stage design", "costume design", "makeup artistry", 
      "special effects", "visual effects", "motion capture", "virtual production", 
      "voice acting", "puppetry", "mime", "improvisation", "stand-up comedy", "satire", 
      "parody", "slapstick", "absurdism", "farce", "musical theater", "opera", "ballet", 
      "modern dance", "hip-hop dance", "tap dance", "ballroom dance", "folk dance", 
      "contemporary dance", "choreography", "dance therapy", "somatics", "martial arts", 
      "yoga", "meditation", "mindfulness", "holistic health", "naturopathy", "homeopathy", 
      "ayurveda", "traditional Chinese medicine", "acupuncture", "herbal medicine", "aromatherapy", 
      "reflexology", "reiki", "crystal healing", "energy medicine", "biofeedback", "hypnotherapy", 
      "sound healing", "art therapy", "music therapy", "drama therapy", "play therapy", 
      "adventure therapy", "wilderness therapy", "animal-assisted therapy", "horticulture therapy", 
      "nutrition therapy", "sports medicine", "physical therapy", "occupational therapy", 
      "speech therapy", "respiratory therapy", "cardiovascular health", "diabetes management", 
      "cancer treatment", "autoimmune diseases", "infectious diseases", "chronic pain management", 
      "geriatric care", "palliative care", "end-of-life care", "sleep disorders", "mental health", 
      "substance abuse", "eating disorders", "child development", "adolescent psychology", 
      "adult development", "gerontology", "family therapy", "couples therapy", "group therapy", 
      "psychopharmacology", "neuroplasticity", "brain-computer interface", "transhumanism", 
      "bioethics", "neuroethics", "genetic counseling", "biostatistics", "epidemiology", 
      "public health", "global health", "health informatics", "telemedicine", "digital health", 
      "wearable technology", "health economics", "health policy", "healthcare administration", 
      "medical education", "clinical trials", "evidence-based medicine", "patient advocacy", 
      "community health", "health equity", "social determinants of health", "health disparities", 
      "disability studies", "inclusive design", "universal design", "assistive technology", 
      "adaptive sports", "paralympic games", "special olympics", "accessible travel", 
      "inclusive education", "diversity and inclusion", "cultural competence", "multiculturalism", 
      "cross-cultural communication", "intercultural relations", "global citizenship", 
      "international relations", "diplomacy", "peace studies", "conflict resolution", 
      "negotiation", "mediation", "arbitration", "human rights", "social justice", 
      "environmental justice", "economic justice", "gender equality", "racial equality", 
      "LGBTQ+ rights", "disability rights", "children's rights", "indigenous rights", 
      "animal rights", "environmental sustainability", "corporate social responsibility", 
      "ethical leadership", "social entrepreneurship", "impact investing", "philanthropy", 
      "volunteerism", "community organizing", "grassroots movements", "advocacy", 
      "policy analysis", "public administration", "governance", "public management", 
      "e-governance", "smart governance", "participatory governance", "collaborative governance", 
      "network governance", "transparency", "accountability", "anti-corruption", "open data", 
      "data privacy", "cyber law", "intellectual property", "patent law", "trademark law", 
      "copyright law", "digital rights", "internet freedom", "media literacy", "information literacy", 
      "critical thinking", "creative problem solving", "innovation management", "design thinking", 
      "lean startup", "agile methodology", "project management", "product management", 
      "business strategy", "competitive analysis", "market research", "consumer behavior", 
      "branding", "advertising", "public relations", "sales management", "customer service", 
      "supply chain management", "logistics", "operations management", "quality management", 
      "risk management", "crisis management", "change management", "organizational behavior", 
      "human resource management", "talent management", "performance management", 
      "employee engagement", "workplace culture", "remote work", "flexible work", 
      "work-life balance", "professional development", "career planning", "leadership development", 
      "succession planning", "executive coaching", "mentorship", "networking", 
      "personal branding", "financial planning", "investment strategies", "retirement planning", 
      "estate planning", "tax planning", "insurance planning", "real estate", 
      "property management", "home improvement", "interior decoration", "gardening", 
      "landscaping", "home automation", "smart home technology", "DIY projects", 
      "crafts", "hobbies", "collecting", "board games", "card games", "video games", 
      "sports", "outdoor recreation", "camping", "hiking", "fishing", "hunting", 
      "boating", "sailing", "scuba diving", "snorkeling", "surfing", "skateboarding", 
      "snowboarding", "skiing", "mountaineering", "rock climbing", "bouldering", 
      "trail running", "marathon running", "triathlon", "ironman", "cycling", 
      "mountain biking", "road biking", "swimming", "water polo", "synchronized swimming", 
      "diving", "gymnastics", "cheerleading", "yoga", "pilates", "aerobics", 
      "strength training", "bodybuilding", "powerlifting", "crossfit", "functional fitness", 
      "high-intensity interval training", "calisthenics", "martial arts", "boxing", 
      "kickboxing", "taekwondo", "karate", "judo", "jiu-jitsu", "muay thai", 
      "wrestling", "sumo wrestling", "fencing", "archery", "shooting", "hunting", 
      "equestrian sports", "horse racing", "polo", "show jumping", "dressage", 
      "rodeo", "bull riding", "barrel racing", "team roping", "calf roping", 
      "ranch sorting", "cowboy action shooting", "reining", "cutting", "working cow horse", 
      "freestyle reining", "reined cow horse", "ranch riding", "trail riding", 
      "endurance riding", "pleasure riding", "driving", "carriage driving", 
      "combined driving", "pleasure driving", "team driving", "draft horse driving", 
      "hackney horse", "shetland pony", "welsh pony", "miniature horse", "falabella horse", 
      "paint horse", "quarter horse", "appaloosa horse", "arabian horse", 
      "thoroughbred horse", "warmblood horse", "friesian horse", "andalusian horse", 
      "lusitano horse", "lipizzaner horse", "haflinger horse", "fjord horse", 
      "connemara pony", "new forest pony", "highland pony", "fell pony", 
      "dales pony", "dartmoor pony", "exmoor pony", "suffolk punch", "cleveland bay", 
      "shire horse", "clydesdale horse", "percheron horse", "belgian horse", 
      "boulonnais horse", "ardennais horse", "comtois horse", "auxois horse", 
      "italian heavy draft", "norwegian fjord horse", "american cream draft horse", 
      "haflinger", "hafling pony", "hackney horse", "hackney pony", "trotter", 
      "pacer", "harness horse", "standardbred horse", "roadster horse", 
      "roadster pony", "saddle seat horse", "saddle seat pony", "fine harness horse", 
      "fine harness pony", "pleasure harness horse", "pleasure harness pony", 
      "draft horse", "heavy horse", "plow horse", "working horse", "farm horse", 
      "riding horse", "driving horse", "pony", "miniature pony", "dwarf horse", 
      "small horse", "large pony", "small pony", "medium pony", "large horse", 
      "small draft horse", "medium draft horse", "large draft horse", "medium light horse", 
      "light horse", "heavy light horse", "medium heavy horse", "heavy heavy horse", 
      "small heavy horse", "medium heavy horse", "large heavy horse", "small light horse", 
      "medium light horse", "large light horse", "small medium light horse", 
      "medium large light horse", "large medium light horse", "small large light horse", 
      "large small light horse", "medium large heavy horse", "large medium heavy horse", 
      "small medium heavy horse", "medium small heavy horse", "small large heavy horse", 
      "large small heavy horse", "medium large medium horse", "large medium medium horse", 
      "small medium medium horse", "medium small medium horse", "small large medium horse", 
      "large small medium horse", "medium large small horse", "large medium small horse", 
      "small medium small horse", "medium small small horse", "small large small horse", 
      "large small small horse", "medium large tiny horse", "large medium tiny horse", 
      "small medium tiny horse", "medium small tiny horse", "small large tiny horse", 
      "large small tiny horse", "medium large giant horse", "large medium giant horse", 
      "small medium giant horse", "medium small giant horse", "small large giant horse", 
      "large small giant horse", "medium large huge horse", "large medium huge horse", 
      "small medium huge horse", "medium small huge horse", "small large huge horse", 
      "large small huge horse", "medium large enormous horse", "large medium enormous horse", 
      "small medium enormous horse", "medium small enormous horse", "small large enormous horse", 
      "large small enormous horse", "medium large tiny pony", "large medium tiny pony", 
      "small medium tiny pony", "medium small tiny pony", "small large tiny pony", 
      "large small tiny pony", "medium large giant pony", "large medium giant pony", 
      "small medium giant pony", "medium small giant pony", "small large giant pony", 
      "large small giant pony", "medium large huge pony", "large medium huge pony", 
      "small medium huge pony", "medium small huge pony", "small large huge pony", 
      "large small huge pony", "medium large enormous pony", "large medium enormous pony", 
      "small medium enormous pony", "medium small enormous pony", "small large enormous pony", 
      "large small enormous pony", "medium large tiny horse", "large medium tiny horse", 
      "small medium tiny horse", "medium small tiny horse", "small large tiny horse", 
      "large small tiny horse", "medium large giant horse", "large medium giant horse", 
      "small medium giant horse", "medium small giant horse", "small large giant horse", 
      "large small giant horse", "medium large huge horse", "large medium huge horse", 
      "small medium huge horse", "medium small huge horse", "small large huge horse", 
      "large small huge horse", "medium large enormous horse", "large medium enormous horse", 
      "small medium enormous horse", "medium small enormous horse", "small large enormous horse", 
      "large small enormous horse", "medium large tiny pony", "large medium tiny pony", 
      "small medium tiny pony", "medium small tiny pony", "small large tiny pony", 
      "large small tiny pony", "medium large giant pony", "large medium giant pony", 
      "small medium giant pony", "medium small giant pony", "small large giant pony", 
      "large small giant pony", "medium large huge pony", "large medium huge pony", 
      "small medium huge pony", "medium small huge pony", "small large huge pony", 
      "large small huge pony", "medium large enormous pony", "large medium enormous pony", 
      "small medium enormous pony", "medium small enormous pony", "small large enormous pony", 
      "large small enormous pony", "medium large tiny horse", "large medium tiny horse", 
      "small medium tiny horse", "medium small tiny horse", "small large tiny horse", 
      "large small tiny horse", "medium large giant horse", "large medium giant horse", 
      "small medium giant horse", "medium small giant horse", "small large giant horse", 
      "large small giant horse", "medium large huge horse", "large medium huge horse", 
      "small medium huge horse", "medium small huge horse", "small large huge horse", 
      "large small huge horse", "medium large enormous horse", "large medium enormous horse", 
      "small medium enormous horse", "medium small enormous horse", "small large enormous horse", 
      "large small enormous horse", "medium large tiny pony", "large medium tiny pony", 
      "small medium tiny pony", "medium small tiny pony", "small large tiny pony", 
      "large small tiny pony", "medium large giant pony", "large medium giant pony", 
      "small medium giant pony", "medium small giant pony", "small large giant pony"
    ]

  def __call__(self):
    return self.search_queries