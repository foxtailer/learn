import csv
import os
import glob

CSV_TITLE = [
  'Product number', 
  'Thumbnail path', 
  'Product title',
  'Detailed picture path',
  'Product description',
  'Reference price',
  'origin URL'
]

def get_script_directory():
    # Get the full path to the script
    script_path = os.path.realpath(__file__)
    # Get the directory containing the script
    script_dir = os.path.dirname(script_path)
    return script_dir

def traverse_folders(root_directory):
    """
    Traverse through all directories in the root_directory without searching in subdirectories.
    Args:
    root_directory (str): The root directory to list directories from.
    Returns:
    list: A list of directory paths.
    """
    directories = [os.path.join(root_directory, d) for d in os.listdir(root_directory) if os.path.isdir(os.path.join(root_directory, d))]
    return directories

def find_and_read_txt_file(directory):
    """
    Find the first .txt file in a given directory and read its contents.
    Args:
    directory (str): The directory to search for the .txt file.  
    Returns:
    str: The content of the first .txt file found, or an empty string if no .txt file is found.
    """
    txt_files = glob.glob(os.path.join(directory, '*.txt'))
    if txt_files:
        with open(txt_files[0], 'r') as file:
            return file.read()
    return ""

def main():
  root_dir = get_script_directory()
  sub_directories = traverse_folders(root_dir)
  urls = {}
  for directory in sub_directories:
      urls[directory - root_dir] = find_and_read_txt_file(directory)

  return urls

print(main())

# def read_text_files(root_directory):
#     folder_texts = {}

#     # Traverse through all directories and subdirectories
#     for dirpath, dirnames, filenames in os.walk(root_directory):
#         # Find all .txt files in the current directory
#         txt_files = glob.glob(os.path.join(dirpath, '*.txt'))
        
#         # Check if there is at least one .txt file in the current directory
#         if txt_files:
#             folder_name = os.path.basename(dirpath)
#             # Read the first .txt file found in the directory
#             file_path = txt_files[0]
#             with open(file_path, 'r') as file:
#                 content = file.read()
#                 folder_texts[folder_name] = content

#     return folder_texts

#  Save CSV file

# data = [
#   CSV_TITLE,
#   [1]*len(CSV_TITLE)
# ]
# with open('output.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

# data = [
#     {'Name': 'Alice', 'Age': 30, 'City': 'New York'},
#     {'Name': 'Bob', 'Age': 25, 'City': 'Los Angeles'},
#     {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}
# ]
# with open('output_dict.csv', 'w', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=['Name', 'Age', 'City'])
#     writer.writeheader()
#     writer.writerows(data)
