import zipfile
import os

def extractor(patn_to_folder):
  """Extract all zip files in folder"""

  for root, dirs, files in os.walk(patn_to_folder, topdown=False):
    for name in files:
      with zipfile.ZipFile(patn_to_folder + "\\" + name, 'r') as zip_ref:
          zip_ref.extractall(r"D:\torrent\New folder\TemplatesBox_84_Flash_Templates" + "\\" + name.replace(".zip", ""))
      
    

extractor(r"D:\torrent\New folder\TemplatesBox_84_Flash_Templates\TemplatesBox.com\FlashEnabledTemplates")