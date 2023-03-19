#!/usr/bin/env python3

import os
import sys
import time
import shutil
from PIL import Image
import imagehash
from termcolor import colored # color Error messages
import subprocess


def og_path(path):
  if not os.path.exists(sys.argv[1]):
    print(colored("ERROR: The path you provided doesn't exist. Please try again", 'red'))
    sys.exit()
  elif len(os.listdir(path)) == 0:
    print(colored("ERROR: Your provided folder is empty! Please try again", 'red'))
    sys.exit()
  elif len(sys.argv) > 2:
    print(colored("ERROR: too more arguments bro", 'red'))
    sys.exit()
  else:
    path = sys.argv[1]
    return path

def remove_dup():
  nn = 0
  try:
    og_path(sys.argv[1]) # just check errors?
    dup = sys.argv[1].split('/')[-2] + '_duplicated/' # dup dir name
  except:
    print(colored('ERROR: Please provide your folder path to check for duplicates\nfor example: images/', 'red'))
    sys.exit()

  if not os.path.exists(dup): # create new folder to store duplicate files
    os.makedirs(dup)
  else:
    dup = str(input("\nSeems you have duplicated/ folder here!\nEnter a new name of the folder to store duplicate files:\n"))
    os.makedirs(dup)
  image_hashes, errors, count = {}, [], 0
  for filename in os.listdir(path):
    file_type = ('jpg', 'png', 'jpeg', 'JPG', 'PNG', 'JPEG') #TODO other file(images) types
    # file_types = ['jpg', 'jpeg', 'png', 'bmp', 'gif', 'tiff', 'svg', 'webp', 'ico', 'jfif', 'pjpeg', 'pjp', 'avif', 'heif', 'pdf', 'eps', 'raw', 'cr2', 'nef', 'orf', 'sr2', 'pef', 'x3f', 'arw', 'rw2', 'dng', 'svgz', 'JPG', 'JPEG', 'PNG', 'BMP', 'GIF', 'TIFF', 'SVG', 'WEBP', 'ICO', 'JFIF', 'PJPEG', 'PJP', 'AVIF', 'HEIF', 'PDF', 'EPS', 'RAW', 'CR2', 'NEF', 'ORF', 'SR2', 'PEF', 'X3F', 'ARW', 'RW2', 'DNG', 'SVGZ']

    if filename.endswith(file_type):
      with Image.open(path + filename) as img:
        hash = str(imagehash.average_hash(img)) #print('Hash data:', hash)
  
        # If the hash is already in the dictionary, delete the file
        if hash in image_hashes:
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
          print(f'Added file to dictionary: {filename}\n')
  print(colored(f"\nFOUND ALL [{nn}] DUPLICATED PICS AND SUCCEED MOVING THOSE TO {dup}", 'green'))
  time.sleep(1)
  subprocess.run(["open", dup])


if __name__ == '__main__':
  remove_dup()
  sys.exit(0)
