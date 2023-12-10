#!/usr/bin/env python3
import os
import sys
import time
import shutil
from PIL import Image
import imagehash
from termcolor import colored # color ERROR messages
import subprocess


def og_path():
  if len(sys.argv) < 2:
    print(colored('ERROR: Please provide your folder path to check for duplicates\nfor example: images/', 'red'))
    sys.exit()

  path = sys.argv[1]

  if not os.path.exists(path):
    print(colored("ERROR: The path you provided doesn't exist. Please try again", 'red'))
    sys.exit()
  elif len(os.listdir(path)) == 0:
    print(colored("ERROR: Your provided folder is empty! Please try again", 'red'))
    sys.exit()
  elif len(sys.argv) > 2:
    print(colored("ERROR: too more arguments bro", 'red'))
    sys.exit()
  else:
    return path

def remove_dup():
  nn, path = 0, og_path() # Set the path variable to the value returned by og_path
  dup = path.split('/')[-2] + '_duplicated/' # dup dir name
  while os.path.exists(dup):
    dup = str(input("\nThere is already a folder named `{}`\nEnter a new name for the folder to store duplicate files:\n".format(dup)))
  os.makedirs(dup)
  image_hashes, errors, count = {}, [], 0
  for filename in os.listdir(path):
    file_type = ('jpg', 'png', 'jpeg', 'JPG', 'PNG', 'JPEG') #TODO other file(images) types
    # file_types = ['jpg', 'jpeg', 'png', 'bmp', 'gif', 'tiff', 'svg', 'webp', 'ico', 'jfif', 'pjpeg', 'pjp', 'avif', 'heif', 'pdf', 'eps', 'raw', 'cr2', 'nef', 'orf', 'sr2', 'pef', 'x3f', 'arw', 'rw2', 'dng', 'svgz', 'JPG', 'JPEG', 'PNG', 'BMP', 'GIF', 'TIFF', 'SVG', 'WEBP', 'ICO', 'JFIF', 'PJPEG', 'PJP', 'AVIF', 'HEIF', 'PDF', 'EPS', 'RAW', 'CR2', 'NEF', 'ORF', 'SR2', 'PEF', 'X3F', 'ARW', 'RW2', 'DNG', 'SVGZ']

    if filename.endswith(file_type):
      with Image.open(path + filename) as img:
        hash = str(imagehash.average_hash(img)) #print('Hash data:', hash)
  
        if hash in image_hashes: # delete file if the hash is already in the dictionary
          print("---> Find duplicate file:", filename)
          try:
            shutil.move(path + filename, dup)
            nn += 1
            print(colored('>>>>> ') + colored(f'Moved duplicate file [{filename}] to directory: {dup}/\n', 'cyan'))
          except:
            print(colored('>>>>> ERROR MOVING FILE TO TRASH <<<<<\n', 'red'))
            errors.append(filename)
        else:
          image_hashes[hash] = filename
          print(f'Added file to dictionary: {filename}')
  print(colored(f"\nFOUND ALL [{nn}] DUPLICATED PICS AND SUCCEED MOVING THOSE TO {dup}", 'green'))
  time.sleep(1)
  subprocess.run(["open", dup])


if __name__ == '__main__':
  remove_dup()
  sys.exit(0)
