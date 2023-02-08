import requests
import hashlib
import urllib.request
from tqdm import tqdm
import os

# Steps:
# Check is this file current
# Then check if all other files are current
# Check if any files are deleted
# Check if there are any new files

def update():
    ''' Starts the update process'''

    url = "https://raw.githubusercontent.com/data4n6s/dailydiary/main/"
    print("Checking for updates.")
    if update_me(url) == True:
        print("Updated check_for_updates.py...")
        update()
    else:
        print("First Step Complete...")

def update_me(url):
    ''' Checks if the Update file: check_for_updates.py has any updates'''

    file = os.path.basename(__file__)
    if isUpToDate(__file__, url+file) == False:
        print("Updates found...")
        update_files(__file__, url+file)
        return True
    else:
        return False

def isUpToDate(fileName,url):

    with open(fileName, "r") as f:
        file = f.read()
    hash = hashlib.sha256((file).encode('utf-8')).hexdigest()
    urlcode = requests.get(url).text
    urlhash = hashlib.sha256((urlcode).encode('utf-8')).hexdigest()
    if hash == urlhash:
        return True
    else:
        return False

def update_files(path, url):
    for i in tqdm(range(1), desc="Downloading Updates..."):
        urllib.request.urlretrieve(url, path)


def checkForUpdates(fileName):

    if isUpToDate(fileName, url) == False:
        update(path, url)
        return True
    else:
        return False