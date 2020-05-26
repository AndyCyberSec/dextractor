#AndyCyberSec 2020 - https://github.com/AndyCyberSec

from zipfile import ZipFile
import sys
import os
import subprocess

def banner():

    print("""Usage: dextractor.py file.apk""")

def dextract(apk):

    dest_path = os.path.dirname(apk)

    if len(dest_path) == 0:
        dest_path = "."

    dexs = []
    file_found = False

    try:
        with ZipFile(apk, 'r') as zip:
            for element in zip.infolist():
                if ".dex" in element.filename:
                    try:
                        zip.extract(element, dest_path)
                        print("[+] Extraction of " + element.filename + " complete!")
                        dexs.append(dest_path + "/" + element.filename)    
                        file_found = True
                    except:
                        print("[-] Error during extraction of " + element.filename)
    except FileNotFoundError:
        print("[-] %s not found :\'( \n" % apk)
    
    if file_found:
        dextojar(dexs, dest_path)

def dextojar(dexs, dest_path):

    print("[+] Now decompiling dex files...\n")

    cmd = ['/usr/local/bin/d2j-dex2jar', ",".join(dexs)]
    stream = subprocess.Popen(cmd, cwd=dest_path)
    stream.wait()
    print("[+] Decompiling complete!\n")
