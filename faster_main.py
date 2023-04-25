#!/usr/bin/env python3

import os
import sys
import time
import shutil
from PIL import Image
import imagehash
from termcolor import colored # color ERROR messages
import subprocess
import threading


def og_path():
    if len(sys.argv) < 2:
        print(colored('ERROR: Please provide your folder path to check for duplicates\nfor example: images/', 'red'))
        sys.exit()

    path = sys.argv[1]
    num_in_path = os.listdir(path)
    print(colored(f"\nChecking ==> {len(num_in_path)} <== of files in {path}", 'green'))

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


def process_file(filename, path, dup, image_hashes, nn, errors):
    file_type = ('jpg', 'png', 'jpeg', 'JPG', 'PNG', 'JPEG') #TODO other file(images) types

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

def remove_dup():
    nn, path = 0, og_path() # Set the path variable to the value returned by og_path
    dup = path.split('/')[-2] + '_duplicated/' # dup dir name
    while os.path.exists(dup):
        dup = str(input("\nThere is already a folder named `{}`\nEnter a new name for the folder to store duplicates:\n".format(dup)))
    os.makedirs(dup)
    image_hashes, errors, count = {}, [], 0

    # Create a list to store the threads
    threads = []

    for filename in os.listdir(path):
        # Create a new thread for each file and start it
        t = threading.Thread(target=process_file, args=(filename, path, dup, image_hashes, nn, errors))
        t.start()
        threads.append(t)

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print(colored(f"\nFOUND ALL [{nn}] DUPLICATED PICS AND SUCCEED MOVING THOSE TO {dup}", 'green'))
    time.sleep(1)
    subprocess.run(["open", dup])

if __name__ == '__main__':
    remove_dup()
    sys.exit(0)

