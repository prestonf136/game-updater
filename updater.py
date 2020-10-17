import requests
import zipfile 
from pyunpack import Archive
import os, sys, stat
import pathlib
uvars = {
    "main":"http://127.0.0.1:8000",
    "fallback":"http://127.0.0.1:8000",
    "dataendpoint":"/serverdata/",
    "versionfile":"version.txt",
    "mainzip":"/gameserver.7z",
    "version":"v0.0.0",
    "folderts":"./downloaded",
    "extracted":"/extraced/",
    "extractedname":"test.exe"
}

def CheckVersion(vs):
    try:
        r = requests.get(uvars["main"]+uvars["dataendpoint"]+uvars["versionfile"])
        if (vs == r.text):
            return True
        else:
            return r.text
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

        Archive(uvars["folderts"]+uvars["mainzip"]).extractall(uvars["folderts"]+uvars["extracted"])
        os.remove(uvars["folderts"]+uvars["mainzip"])
    except:
        r = requests.get(uvars["fallback"]+uvars["dataendpoint"]+uvars["versionfile"])
        open(uvars["folderts"]+uvars["mainzip"], "wb").write(r.content)

        Archive(uvars["folderts"]+uvars["mainzip"]).extractall(uvars["folderts"]+uvars["extracted"])
        os.remove(uvars["folderts"]+uvars["mainzip"])

def PlayFiles():
    os.system(str(pathlib.Path().absolute())+"/downloaded"+uvars["extracted"]+uvars["extractedname"])

