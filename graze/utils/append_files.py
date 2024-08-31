""" consolidates all file present in a directory into a big file """

import os
current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)

def consolidate(input_directory:str, output_file:str):
  files = os.listdir(input_directory)

  with open(output_file, 'a', encoding='utf-8') as output_file:
    for file_name in files:
      input_path = os.path.join(input_directory, file_name)

      if file_name.endswith('.txt') and os.path.isfile(input_path):
        print(f"Reading: {file_name}")
        with open(input_path, 'r', encoding='utf-8') as input_file:
          output_file.write(input_file.read())
          output_file.write('\n')

        print(f"Reading complete: {file_name}")
      else:
        print(f"Skipping non-text file: {file_name}")