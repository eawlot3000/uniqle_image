#!/usr/bin/env python3
import os
import sys
import time
import shutil
from PIL import Image
import imagehash
from termcolor import colored # color Error messages
import subprocess
from concurrent.futures import ThreadPoolExecutor
import threading

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

def remove_dup(filename):
  nn = 0
  path = sys.argv[1]
  default_path = og_path(sys.argv[1]).split('/')[-2]
  dup = default_path + '_duplicated'
  image_hashes, errors, count = {}, [], 0
  file_type = ('jpg', 'png', 'jpeg', 'JPG', 'PNG', 'JPEG')
  if filename.endswith(file_type):
    with Image.open(path + filename) as img:
      hash = str(imagehash.average_hash(img))
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
  return nn

def main():
  try:
    path = sys.argv[1] # TODO: should ask [user] where the images folder is
    default_path = og_path(sys.argv[1]).split('/')[-2]
    dup = default_path + '_duplicated'
    #print(default_path, dup)
  except:
    print(colored('ERROR: Please provide your folder path to check for duplicates\nfor example: images/', 'red'))
    sys.exit()

  if not os.path.exists(dup): # create new folder to store duplicate files
    os.makedirs(dup)
  else:
    dup = str(input("\nSeems you have duplicated/ folder here!\nEnter a new name of the folder to store duplicate files:\n"))
    os.makedirs(dup)

  # Get the list of filenames to process
  filenames = os.listdir(path)

  # Create a thread pool with 64 worker threads
  nn = 0
  lock = threading.Lock()
  with ThreadPoolExecutor(max_workers=64) as executor:
    for filename in filenames:
      # Submit the remove_dup() function to the thread pool
      future = executor.submit(remove_dup, filename)

      # Wait for the thread to complete before moving on to the next file
      nn += future.result()

  print(colored(f"\nFOUND ALL [{nn}] DUPLICATED PICS AND SUCCEED MOVING THOSE TO {dup}", 'green'))
  time.sleep(1)
  subprocess.run(["open", dup])



if __name__ == '__main__':
  main()
  sys.exit(0)


