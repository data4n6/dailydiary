import requests
from github import Github
import os
import shutil
import urllib.request 
from config import token, username, url, repo
from tqdm import tqdm



version = "v1.0.1"
g = Github(token)
user_data = requests.get(url, auth=(username,token)).json()
tag = user_data[0]["tag_name"]
repository = g.get_user(username).get_repo(repo)
local_dir = "python-files"

# About
print("="*50)
print("Full name:", repository.full_name)
print("Description:", repository.description)
print("Date created:", repository.created_at)
print("Date of last push:", repository.pushed_at)
print("Home Page:", repository.homepage)
print("Language:", repository.language)
print("Number of forks:", repository.forks)
print("Number of stars:", repository.stargazers_count)
print("-"*50)

def does_path_exists(path):
    ''' Checks to see if the path exists'''
    
    if os.path.exists(path):
        print(f"Yes {path} exists, sending True")
        return True
    else:
        print(f"No {path} does not exist, sending False")
        return False

def update_file(url, filenamepath):
    for i in tqdm(range(1), desc=f"Downloading Updates for {filenamepath}..."):
        urllib.request.urlretrieve(url, filenamepath)
        
        
def download_directory(repository, local_dir,delete_dir=True,remote_dir=""):
    """
    Download all contents from github with latest tag from repository.
    """
    print(f"Delete Dir: {delete_dir}")
    if delete_dir:
        try:
            if does_path_exists(local_dir):
                shutil.rmtree(local_dir)
                print(f"{local_dir} deleted.")
        except:
            pass

        finally: 
            os.makedirs(local_dir)
            print(f"{local_dir} created.")            

    elif does_path_exists(local_dir):
        print(f"Path: {local_dir} exists. Do Nothing")
        pass
    else:
        os.makedirs(local_dir)
        print(f"{local_dir} created.") 

    for content in repository.get_contents(remote_dir):
        if content.type == "dir":
            path = os.path.join(local_dir,content.path)
            print(f"Found Dir: {content.path}")
            print(f"Need to Create Path: {path}")
            if does_path_exists(path):
                print(f"Path: {path} exists. Do Nothing")
                pass
            else:
                os.makedirs(path)
                print(f"{path} created.") 
            download_directory(repository,local_dir,False,content.path)
        else:
            filenamepath = os.path.join("python-files",content.path)
            update_file(content.download_url, filenamepath)
            

if tag > version:
    download_directory(repository, local_dir)
else:
    pass