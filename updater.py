import requests
import zipfile 
from pyunpack import Archive
import os

uvars = {
    "main":"http://127.0.0.1:8000",
    "fallback":"http://127.0.0.1:8000",
    "dataendpoint":"/serverdata/",
    "versionfile":"version.txt",
    "mainzip":"/main.txt.7z",
    "version":"v0.0.0",
    "folderts":"./downloaded"
}

def CheckVersion(vs):
    try:
        print(vars["main"]+uvars["dataendpoint"]+uvars["versionfile"])
        r = requests.get(uvars["main"]+uvars["dataendpoint"]+uvars["versionfile"])
        if (vs == r.text):
            return True
        else:
            return False
    except:
        r = requests.get(uvars["fallback"]+uvars["dataendpoint"]+uvars["versionfile"])
        if (vs == r.text):
            return True
        else:
            return False

def UpdateFiles():
    try:
        r = requests.get(uvars["main"]+uvars["dataendpoint"]+uvars["mainzip"], allow_redirects=True)
        open(uvars["folderts"]+uvars["mainzip"], "wb").write(r.content)

        Archive(uvars["folderts"]+uvars["mainzip"]).extractall(uvars["folderts"]+"/extraced")
        os.remove(uvars["folderts"]+uvars["mainzip"])
    except:
        r = requests.get(uvars["fallback"]+uvars["dataendpoint"]+uvars["versionfile"])
        open(uvars["folderts"]+uvars["mainzip"], "wb").write(r.content)

        Archive(uvars["folderts"]+uvars["mainzip"]).extractall(uvars["folderts"]+"/extraced")
        os.remove(uvars["folderts"]+uvars["mainzip"])

if CheckVersion(uvars["version"]):
    print("no update needed")
else:
    UpdateFiles()