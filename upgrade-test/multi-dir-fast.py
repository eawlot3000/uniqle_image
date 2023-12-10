#!/usr/bin/env python3

import os
import sys
import time
import shutil
from PIL import Image
import imagehash
from termcolor import colored  # color ERROR messages
import subprocess
import threading


def og_path():
  if len(sys.argv) < 2:
    print(colored('ERROR: Please provide at least one folder path to check for duplicates\nfor example: images/', 'red'))
    sys.exit()

  paths = sys.argv[1:]
  num_in_paths = [os.listdir(p) for p in paths]
  total_num_files = sum(len(num) for num in num_in_paths)
  check_confirm = str(input(colored(f"\nReady to check ==> {total_num_files} <== files in {len(paths)} folders: {', '.join(paths)} [Y/N]", 'green')))
  if check_confirm.lower() != 'y':
    sys.exit()
  else:
    for path in paths:
      if not os.path.exists(path):
        print(colored(f"ERROR: The path {path} doesn't exist. Skipping...", 'red'))
      elif len(os.listdir(path)) == 0:
        print(colored(f"WARNING: The folder {path} is empty! Skipping...", 'yellow'))
      else:
        return path



duplicate_count, dup_lock = 0, threading.Lock() # Define global variables for counting duplicates

def process_file(filename, path, dup, image_hashes, errors):
  global duplicate_count
  file_type = ('jpg', 'png', 'jpeg', 'JPG', 'PNG', 'JPEG')  # TODO other file(images) types

  if filename.endswith(file_type):
    with Image.open(path + filename) as img:
      hash = str(imagehash.average_hash(img))

      if hash in image_hashes:
        print("---> Find duplicate file:", filename)
        try:
          shutil.move(path + filename, dup)
          with dup_lock:
            duplicate_count += 1
          print(colored('>>>>> ') + colored(f'Moved duplicate file [{filename}] to directory: {dup}/\n', 'cyan'))
        except:
          print(colored('>>>>> ERROR MOVING FILE TO TRASH <<<<<\n', 'red'))
          errors.append(filename)
      else:
        image_hashes[hash] = filename
        print(f'Added file to dictionary: {filename}')


def remove_dup():
  path = og_path() 
  dup = path.split('/')[-2] + '_duplicated/'
  while os.path.exists(dup):
    dup = str(input("\nThere is already a folder named `{}`\nEnter a new name for the folder to store duplicates:\n".format(dup)))
  os.makedirs(dup)
  image_hashes, errors, threads = {}, [], []

  MAX_THREADS = 64  # ==> modify this to your desired number of threads accordingly!

  for filename in os.listdir(path):
    t = threading.Thread(target=process_file, args=(filename, path, dup, image_hashes, errors))
    t.start()
    threads.append(t)
    while len(threads) >= MAX_THREADS:
      # Wait for any threads to complete
      for t in threads:
        t.join(0.1)  # Adjust the timeout value as needed
      threads = [t for t in threads if t.is_alive()] # Remove completed threads from the list

  for t in threads: # Wait for all remaining threads to complete
    t.join()

  print(colored(f"\nFOUND ALL [{duplicate_count}] DUPLICATED PICS AND SUCCEED MOVING THOSE TO {dup}", 'green'))
  time.sleep(1)
  subprocess.run(["open", dup])


if __name__ == '__main__':
  remove_dup()
  sys.exit(0)
