import os
import shutil
import gzip

current_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_directory)

def unzip(input_directory:str, output_directory:str):
  os.makedirs(output_directory, exist_ok=True)
  files = os.listdir(input_directory)

  for file_name in files:
    input_path = os.path.join(input_directory, file_name)
    output_path = os.path.join(output_directory, os.path.splitext(file_name)[0])

    if file_name.endswith('.gz'):
      print(f"Unzipping: {file_name}")

      with gzip.open(input_path, 'rb') as f_in:
        with open(output_path, 'wb') as f_out:
          shutil.copyfileobj(f_in, f_out)
          print(f"Unzipping complete: {output_path}")
    else:
      print(f"Skipping non-GZip file: {file_name}")