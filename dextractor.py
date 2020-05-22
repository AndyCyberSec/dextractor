#!/usr/local/bin/python3
#AndyCyberSec 2020 - https://github.com/AndyCyberSec

from zipfile import ZipFile
import sys
import os

def banner():

    print("""Usage: dextractor.py file.apk""")

try:
    apk = sys.argv[1]
except:
    banner()
    sys.exit(0)

dest_path = os.path.dirname(sys.argv[1])

if len(dest_path) == 0:
    dest_path = "."

dexs = []

with ZipFile(apk, 'r') as zip:
    for element in zip.infolist():
        if ".dex" in element.filename:
            try:
                zip.extract(element, dest_path)
                print("[+] Extraction of " + element.filename + " complete!")
                dexs.append(dest_path + "/" + element.filename)    
            except:
                print("[-] Error during extraction of " + element.filename)

print("[+] Now decompiling dex files...")
print(dest_path)
stream = os.popen("/usr/local/bin/d2j-dex2jar " + ",".join(dexs))
stream.read()
print("[+] Decompiling complete!"
