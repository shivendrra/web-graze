import os
current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)
import xml.etree.ElementTree as ET

# Load XML file
tree = ET.parse('xml dumps/enwiki2.xml')
root = tree.getroot()

urls = [link.text for link in root.findall(".//link")]

output_file = 'extracted_urls1.txt'
with open(output_file, 'w', encoding='utf-8') as f:
  for url in urls:
    f.write(url + '\n')

print(f"Extracted URLs saved to {output_file}")